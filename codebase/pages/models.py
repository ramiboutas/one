from django.urls import reverse_lazy

from ..utils.abstracts_and_mixins import AbstractFlatPageModel, AbstractSubmoduleFolder


class PagesFolder(AbstractSubmoduleFolder):
    pass


class Page(AbstractFlatPageModel):
    """File-based page model"""

    def get_absolute_url(self):
        return reverse_lazy("page-detail", kwargs={"slug": self.slug})
