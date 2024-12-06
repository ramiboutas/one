from django.contrib import admin
from django.db.migrations.recorder import MigrationRecorder
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from huey.contrib.djhuey import HUEY
from modeltranslation.admin import TranslationAdmin

from codebase.base.utils.actions import translation_actions
from codebase.base.utils.admin import FORMFIELD_OVERRIDES_DICT

from ..articles.tasks import trigger_sync_articles
from ..pages.tasks import trigger_sync_pages
from .models import ArticlesFolder, ExtendedSite, PagesSubmodule, Traffic


@admin.register(ArticlesFolder)
@admin.register(PagesSubmodule)
class ArticleFolderAdmin(admin.ModelAdmin):
    """
    Leave this here in the base app, because it applies to more than 1 app
    """

    pass


@admin.register(ExtendedSite)
class ExtendedSiteAdmin(TranslationAdmin):
    formfield_overrides = FORMFIELD_OVERRIDES_DICT  # type: ignore
    list_display = ("__str__", "domain", "name")
    search_fields = ("domain", "name")
    readonly_fields = ("last_huey_flush",)
    list_editable = ("domain", "name")
    actions = translation_actions + ["flush_huey", "sync_articles", "sync_pages"]

    fieldsets = (
        (
            _("Site fields"),
            {"fields": ("domain", "name")},
        ),
        (
            _("Management"),
            {
                "fields": (
                    "remarks",
                    "last_huey_flush",
                    "allow_translation",
                    "override_translated_fields",
                    "default_language",
                    "rest_languages",
                )
            },
        ),
        (
            _("Submodules"),
            {"fields": ("article_folders", "page_folders")},
        ),
        (
            _("Brand"),
            {"fields": ("emoji", "emoji_in_brand")},
        ),
        (
            _("Defaults"),
            {"fields": ("page_title", "page_description", "page_keywords")},
        ),
        (
            _("Appearance and design"),
            {
                "fields": (
                    "picocss_color",
                    "footer_links_separator",
                    "change_theme_light_in_navbar",
                    "change_language_in_navbar",
                    "change_theme_light_in_footer",
                    "change_language_in_footer",
                )
            },
        ),
    )

    @admin.action(description="🗑️ Flush Huey | revoke tasks")
    def flush_huey(modeladmin, request, queryset):
        HUEY.flush()
        queryset.update(last_huey_flush=now())

    @admin.action(description="🔄 Sync articles")
    def sync_articles(modeladmin, request, queryset):
        trigger_sync_articles(queryset)

    @admin.action(description="🔄 Sync pages")
    def sync_pages(modeladmin, request, queryset):
        trigger_sync_pages(queryset)


@admin.register(MigrationRecorder.Migration)
class MigrationRecorderAdmin(admin.ModelAdmin):
    list_display = ("name", "app", "applied")
    list_filter = ("app", "applied")


@admin.register(Traffic)
class TrafficAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "request_path",
        "response_status_code",
        "request_method",
        "user",
    )
    list_filter = ("time", "site", "request_method", "response_status_code")
    readonly_fields = (
        "request_GET",
        "request_GET_ref",
        "request_POST",
        "request_path",
        "request_headers",
        "request_country_code",
        "response_headers",
        "response_status_code",
        "request_method",
        "user",
        "site",
        "time",
    )
