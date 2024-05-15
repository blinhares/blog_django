from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from blog.models import Post, Page
from utils.log import log
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView

l = log(__name__)

#Classe Base View - https://docs.djangoproject.com/en/5.0/ref/class-based-views/
# https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#


PER_PAGE = 9

class PostListView(ListView):
    model = Post
    template_name = 'blog/pages/index.html'
    ordering = '-pk',
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published #para utilizar o manager criado no model POst

    # def get_queryset(self):
    #     """Reescrevendo a query para retornar somente os posts publicados"""
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_published=True)
    #     return queryset
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({'page_title':'Home - ',})
        return context

class PageDetailView(DetailView):
    template_name = 'blog/pages/page.html'
    model = Page
    #https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_field
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


def by_tag(request:HttpRequest,tag_slug:str)->HttpResponse:
    """
    View Criado para Post com Determinada TAG
    """
    l.debug('Run by_category View...')
    l.debug(f'Coletando publicações com categoria :{tag_slug}')
    posts = Post.objects\
            .get_published.filter(tags__slug = tag_slug) # type: ignore
    ## __ é usado para buscar dados dentro de um tabela forang key
    l.debug('Dados Coletados')
    l.debug('Iniciando Paginator')
    paginator = Paginator(posts, PER_PAGE) # type: ignore
    l.debug('Coletando numero da pagina')
    page_number = request.GET.get("page")
    l.debug('Retornando Objeto Paginado')
    page_obj = paginator.get_page(page_number)
    l.debug('Renderizando pagina')

    return render(
        request,
        'blog/pages/index.html', #utilizando pagina de index
        {
            'page_obj': page_obj,
            'page_title':f'By Tag : {tag_slug} - '
        }
    )

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
