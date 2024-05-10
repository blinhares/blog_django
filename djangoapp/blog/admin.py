from django.contrib import admin
# from blog.models.tag_model import Tag
# from djangoapp.blog.models.category_model import Category
# from djangoapp.blog.models.page_model import Page
from blog.models import *

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
class PageAdmin(admin.ModelAdmin): # type: ignore
    list_display = 'id','title', 'slug','is_published',
    list_display_links = 'id','title'
    search_fields = list_display
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug':('title',),
        }


