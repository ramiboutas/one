from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Page, PageParentFolder


@admin.register(PageParentFolder)
class PagesSubmoduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(TranslationAdmin):
    list_display = ("title", "folder", "subfolder", "created_on", "updated_on")
    readonly_fields = (
        "title",
        "folder",
        "subfolder",
        "body",
        "created_on",
        "updated_on",
    )
    list_filter = ("folder", "created_on", "updated_on")
    search_fields = ("title", "folder", "subfolder", "body")
