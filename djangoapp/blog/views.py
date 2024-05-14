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

def page(request:HttpRequest)->HttpResponse:
    return render(
        request,
        'blog/pages/page.html',
        {
            # 'page_obj': page_obj,
        }
    )


def post(request:HttpRequest,slug:str)->HttpResponse:
    print('-'*80)
    print(slug)
   
    return render(
        request,
        'blog/pages/post.html',
        {
            # 'page_obj': page_obj,
        }
    )