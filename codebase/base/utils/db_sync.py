from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.utils.text import slugify

from ...sites.models import Site
from .abstracts import BasePageModel
from .telegram import Bot


def sync_page_objects(PageModel: type[BasePageModel], PageModelFile=None, sites=None):
    """
    Read the contents of the specified submodule and save them in the database.
    :param PageModel: Model class to save objects (Page or Article).
    :param PageModelFile: Optional, file model class (Example: ArticleFile).
    :sites Iterable[Site]: Optional, extended sites to sync.
    """

    # Definitions and checks
    SubmoduleModel = PageModel.submodule_model
    submodule_name = SubmoduleModel.submodule_name
    submodule_path = settings.SUBMODULES_PATH / submodule_name

    if not isinstance(submodule_path, Path):
        Bot.to_admin(f"No path for {submodule_name} found. Check SUBMODULES_PATH")
        return

    if not submodule_path.is_dir():
        Bot.to_admin(
            f"The '{submodule_name}' path is not a directory. Check SUBMODULES_PATH"
        )
        return

    if sites is None:
        sites = Site.objects.filter()

    for extsite in sites:
        to_admin = f"🔄 Syncing {submodule_name} for {extsite.name}\n\n"

        folder_list = extsite.get_submodule_folders_as_list(Model=SubmoduleModel)

        if not folder_list or folder_list == []:
            to_admin += (
                f"No folders found for {extsite} while syncing {submodule_name}."
            )
            continue

        # Scanning
        for folder in folder_list:
            folder_path = submodule_path / folder

            if not folder_path.is_dir():
                to_admin += f"🔴 {folder} is not listed\n\n"
                continue

            for subfolder_path in folder_path.iterdir():
                if not subfolder_path.is_dir():
                    continue

                body_replacements = {}
                to_admin += f"✍ {folder}/{subfolder_path.name}\n"

                db_object = PageModel.objects.get_or_create(
                    submodule=SubmoduleModel.objects.get_or_create(name=folder)[0],
                    subfolder=subfolder_path.name,
                    folder=folder,
                )[0]

                db_object.sites.add(extsite)

                # Markdown files (.md) need to be processed first
                for md_file_path in (
                    p for p in subfolder_path.iterdir() if p.name.endswith(".md")
                ):
                    md_file_conventions_ok = all(
                        (
                            md_file_path.name[:2] in settings.LANGUAGE_CODES,
                            len(md_file_path.read_text().split("\n")) > 2,
                            md_file_path.read_text().strip().startswith("#"),
                        )
                    )
                    if not md_file_conventions_ok:
                        to_admin += (
                            f"⚠️ File '{md_file_path.name}' does not meet conventions"
                        )
                        continue

                    lang_code = md_file_path.name[:2]
                    title = (
                        md_file_path.read_text().split("\n")[0].replace("#", "").strip()
                    )
                    body_text = "\n".join(
                        md_file_path.read_text().split("\n")[1:]
                    ).strip()
                    setattr(db_object, f"title_{lang_code}", title)
                    setattr(db_object, f"slug_{lang_code}", slugify(title))
                    setattr(db_object, f"body_{lang_code}", body_text)

                # Process additional files if model is 'article'
                if PageModelFile:
                    for other_file_path in (
                        p
                        for p in subfolder_path.iterdir()
                        if not p.name.endswith(".md")
                    ):
                        db_file = PageModelFile.objects.get_or_create(
                            parent_page=db_object, name=other_file_path.name
                        )[0]
                        db_file.file = File(
                            other_file_path.open(mode="rb"), name=other_file_path.name
                        )
                        db_file.save()
                        body_replacements[f"]({db_file.name})"] = (
                            f"]({db_file.file.url})"
                        )

                    # Adjust body if markdown file includes files
                    for local, remote in body_replacements.items():
                        for lang_code in settings.LANGUAGE_CODES:
                            field = f"body_{lang_code}"
                            if (
                                not hasattr(db_object, field)
                                or getattr(db_object, field) is None
                            ):
                                continue

                            new_value = getattr(db_object, field).replace(local, remote)
                            setattr(db_object, f"body_{lang_code}", new_value)

                # Save all object attributes in the database
                db_object.save()

        Bot.to_admin(to_admin)
