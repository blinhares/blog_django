
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    # path('post/<slug:post_slug>/', post, name='post'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('created_by/<int:user_id>/', CreatedBy.as_view(), name='created_by'),
    path('by_category/<slug:category_slug>/', CategoryListView.as_view(), name='by_category'),
    path('by_tag/<slug:tag_slug>/', by_tag, name='by_tag'),
    path('search/', SearchListVIew.as_view(), name='search'),
]

