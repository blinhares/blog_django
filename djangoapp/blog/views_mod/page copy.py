from blog.views.index import PostListView
from blog.models import Post, Page
from utils.log import log
from django.db.models import Q
from django.contrib.auth.models import User


class PostDetailView(DetailView):
    template_name = 'blog/pages/post.html'
    model = Post
    context_object_name = 'post'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        post = self.get_object()
        ctx.update({
            'page_title':f'{post.title} - ' # type: ignore
        })
        return ctx

# def post(request:HttpRequest,post_slug:str)->HttpResponse:
#     l.debug('Run post View...')
#     l.debug(f'Coletando publicações com slug :{post_slug}')
#     post_obj = Post.objects.get_published.filter(slug=post_slug).first() # type: ignore
#     if post_obj is None:
#         raise Http404()
            
#     return render(
#         request,
#         'blog/pages/post.html',
#         {
#             'post':post_obj,
#             'page_title':f'{post_obj.title} - '
#         },
#     )