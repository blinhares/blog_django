from blog.views.index import PostListView
from blog.models import Post, Page
from utils.log import log
from django.db.models import Q
from django.contrib.auth.models import User


class CreatedBy(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._temp_context:dict[str,Any] = dict()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        user = self._temp_context.get('user')
        
        if user.first_name:
            user_name = f'{user.first_name} {user.last_name}'
        else:
            user_name = user
        
        context.update({
            'page_title':f'By: {user_name} - '
        })

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        #coleta argumentos vindos da requisicao como dict vindo da url.py
        user_id = self.kwargs.get('user_id') 
        user = User.objects.filter(pk=user_id).first()

        if user is None:
            raise Http404()
        
        self._temp_context.update({
            'user_id':user_id,
            'user':user
        })

        return super().get(request, *args, **kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.filter(created_by__pk = self.kwargs.get('user_id'))
        return queryset


# def created_by(request:HttpRequest,user_id:str)->HttpResponse:
#     """
#     View Criado para Pagina do Author
#     """
#     l.debug('Run created_by View...')
#     user = User.objects.filter(pk=user_id).first()
#     if user is None:
#         raise Http404('Usuario Inexistente!')
    
#     if user.first_name:
#         user_name = f'{user.first_name} {user.last_name}'
#     else:
#         user_name = user

#     l.debug(f'Coletando publicações do user_id:{user_id}')
#     posts = Post.objects\
#             .get_published.filter(created_by__pk = user_id) # type: ignore
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
#             'page_title':f'By: {user_name} - '
#         }
#     )