from blog.views.index import PostListView
from blog.models import Post, Page
from utils.log import log
from django.db.models import Q
from django.contrib.auth.models import User

class SearchListVIew(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._search_value = ''

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self._search_value = request.GET.get('search','').strip()

        return super().setup(request, *args, **kwargs)
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter( # type: ignore
                Q(title__icontains = self._search_value)| #Q adiciona um `and` a query
                Q(excerpt__icontains = self._search_value)|
                Q(content__icontains = self._search_value)
                )[:PER_PAGE]
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'search_value':self._search_value,
            'page_title':f'Search : {self._search_value[:10]}... - '
        })
        return ctx
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self._search_value == '':
            return redirect('blog:index')

        return super().get(request, *args, **kwargs)

# def search(request:HttpRequest)->HttpResponse:
#     """
#     View Criado para Pesquisas
#     """
#     l.debug('Run search View...')
#     l.debug('Coletando o valor da busca no formulario de nome "search"...')
    
#     search_value = request.GET.get('search','').strip()

#     l.debug(f'Coletando publicaçõe que contenha o valor buscado ({search_value})')

#     posts = Post.objects\
#             .get_published.filter( # type: ignore
#                 Q(title__icontains = search_value)| #Q adiciona um `and` a query
#                 Q(excerpt__icontains = search_value)|
#                 Q(content__icontains = search_value)
#                 )[:PER_PAGE] #devolve somente um numero limitado de paginas
#     l.debug('Dados Coletados')
    
#     return render(
#         request,
#         'blog/pages/index.html', #utilizando pagina de index
#         {
#             'page_obj': posts,
#             'search_value':search_value,
#             'page_title':f'Search : {search_value[:10]}... - '
#         }
#     )
