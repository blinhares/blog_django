from blog.views.index import PostListView
from blog.models import Post, Page
from utils.log import log
from django.db.models import Q
from django.contrib.auth.models import User

class PageDetailView(DetailView):
    template_name = 'blog/pages/page.html'
    model = Page
    slug_field = 'slug'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        page = self.get_object()
        ctx.update({
            'page_title':f'{page.title} - ' # type: ignore
        })
        return ctx
    


# def page(request:HttpRequest,slug:str)->HttpResponse:
#     l.debug('Run page View...')
#     l.debug(f'Coletando publicações com slug :{slug}')
#     page = Page.objects.filter(is_published=True).\
#         filter(slug=slug).first() # type: ignore
#     if page is None:
#         raise Http404()
    
#     return render(
#         request,
#         'blog/pages/page.html',
#         {
#             'page':page,
#             'page_title':f'{page.title} - '
#         }
        
#     )