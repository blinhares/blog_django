
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:post_slug>/', post, name='post'),
    path('page/<slug:slug>/', page, name='page'),
    path('created_by/<int:user_id>/', created_by, name='created_by'),
    path('by_category/<slug:category_slug>/', by_category, name='by_category'),
    path('by_tag/<slug:tag_slug>/', by_tag, name='by_tag'),
]

