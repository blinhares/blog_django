from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post
from utils.log import log

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
    return render(
        request,
        'blog/pages/page.html',
        
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