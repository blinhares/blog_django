from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page
from utils.log import log
from django.db.models import Q

l = log(__name__)

PER_PAGE = 9
# Create your views here.
def index(request:HttpRequest)->HttpResponse:
    """
    View Criado para Pagina de Index.
    """
    l.debug('Run Index View...')
    l.debug('Coletando dados do Model Post')
    posts = Post.objects\
            .get_published # type: ignore
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
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def page(request:HttpRequest,slug:str)->HttpResponse:
    l.debug('Run page View...')
    l.debug(f'Coletando publicações com slug :{slug}')
    page = Page.objects.filter(is_published=True).\
        filter(slug=slug).first() # type: ignore
    
    return render(
        request,
        'blog/pages/page.html',
        {
            'page':page
        }
        
    )


def post(request:HttpRequest,post_slug:str)->HttpResponse:
    l.debug('Run post View...')
    l.debug(f'Coletando publicações com slug :{post_slug}')
    post = Post.objects.get_published.filter(slug=post_slug).first() # type: ignore
            
    return render(
        request,
        'blog/pages/post.html',
        {
            'post':post,
        },
    )

def created_by(request:HttpRequest,user_id:str)->HttpResponse:
    """
    View Criado para Pagina do Author
    """
    l.debug('Run created_by View...')
    l.debug(f'Coletando publicações do user_id:{user_id}')
    posts = Post.objects\
            .get_published.filter(created_by__pk = user_id) # type: ignore
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
        }
    )

def by_category(request:HttpRequest,category_slug:str)->HttpResponse:
    """
    View Criado para Post com Determinada Categoria
    """
    l.debug('Run by_category View...')
    l.debug(f'Coletando publicações com categoria :{category_slug}')
    posts = Post.objects\
            .get_published.filter(category__slug = category_slug) # type: ignore
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
        }
    )

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
        }
    )

def search(request:HttpRequest)->HttpResponse:
    """
    View Criado para Pesquisas
    """
    l.debug('Run search View...')
    l.debug('Coletando o valor da busca no formulario de nome "search"...')
    
    search_value = request.GET.get('search','').strip()

    l.debug(f'Coletando publicaçõe que contenha o valor buscado ({search_value})')

    posts = Post.objects\
            .get_published.filter( # type: ignore
                Q(title__icontains = search_value)| #Q adiciona um `and` a query
                Q(excerpt__icontains = search_value)|
                Q(content__icontains = search_value)
                )[:PER_PAGE] #devolve somente um numero limitado de paginas
    l.debug('Dados Coletados')
    
    return render(
        request,
        'blog/pages/index.html', #utilizando pagina de index
        {
            'page_obj': posts,
            'search_value':search_value
        }
    )
