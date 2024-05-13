from typing import Any
from django.contrib import admin
# from blog.models.tag_model import Tag
# from djangoapp.blog.models.category_model import Category
# from djangoapp.blog.models.page_model import Page
from blog.models import *
#SummerNote
from django_summernote.admin import SummernoteModelAdmin # type: ignore


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin): # type: ignore
    list_display = 'id','name', 'slug',
    list_display_links = 'id','name'
    search_fields = list_display
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug':('name',),
        }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): # type: ignore
    list_display = 'id','name', 'slug',
    list_display_links = 'id','name'
    search_fields = list_display
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug':('name',),
        }

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin): # type: ignore
    summernote_fields = 'content',
    list_display = 'id','title', 'slug','is_published',
    list_display_links = 'id','title'
    search_fields = list_display
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug':('title',),
        }

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin): # type: ignore
    summernote_fields = 'content',
    list_display = 'id','title','is_published', 'created_by'
    list_display_links = 'id','title',
    search_fields = list_display
    list_per_page = 50
    list_filter = 'category', 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 'created_by', 'updated_by',
    prepopulated_fields = {
        "slug": ('title',),
    }
    autocomplete_fields = 'tags', 'category',

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        """_summary_
        [documentation.](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#modeladmin-methods)
        
        Args:
            request (Any): ...
            obj (Any): ...
            form (Any): ...
            change (Any): bool que descreve se esta alterando ou criando . 
            True para alterar

        Returns:
            None
        """
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user

        return super().save_model(request, obj, form, change) # type: ignore

