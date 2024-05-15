from blog.views.index import PostListView
from blog.models import Post, Page
from utils.log import log
from django.db.models import Q
from django.contrib.auth.models import User

class CategoryListView(PostListView):
    allow_empty = False #retorna um erro em caso de query vazia
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.filter(
            category__slug = self.kwargs.get('category_slug'))
        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'page_title':f'Category : {self.object_list[0].category.name} - ' # type: ignore
        })
        return ctx

# def by_category(request:HttpRequest,category_slug:str)->HttpResponse:
#     """
#     View Criado para Post com Determinada Categoria
#     """
#     l.debug('Run by_category View...')
#     l.debug(f'Coletando publicações com categoria :{category_slug}')
#     posts = Post.objects\
#             .get_published.filter(category__slug = category_slug) # type: ignore
#     ## __ é usado para buscar dados dentro de um tabela forang key
#     if len(posts) == 0:
#         raise Http404()
    
#     l.debug('Dados Coletados')
#     l.debug('Iniciando Paginator')
#     paginator = Paginator(posts, PER_PAGE) # type: ignore
#     l.debug('Coletando numero da pagina')
#     page_number = request.GET.get("page")
#     l.debug('Retornando Objeto Paginado')
#     page_obj = paginator.get_page(page_number)
#     l.debug('Renderizando pagina')

#     return render(
#         request,
#         'blog/pages/index.html', #utilizando pagina de index
#         {
#             'page_obj': page_obj,
#             'page_title':f'Category : {page_obj[0].category.name} - '
#         }
#     )
