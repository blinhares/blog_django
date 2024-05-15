from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Page
from utils.log import log
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import ListView

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


# def index(request:HttpRequest)->HttpResponse:
#     """
#     View Criado para Pagina de Index.
#     """
#     l.debug('Run Index View...')
#     l.debug('Coletando dados do Model Post')
#     posts = Post.objects\
#             .get_published # type: ignore
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
#         'blog/pages/index.html',
#         {
#             'page_obj': page_obj,
#             'page_title':'Home - '
#         }
#     )
