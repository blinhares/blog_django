from django.db import models
from blog.models.tag_model import Tag
from blog.models.category_model import Category
from utils.slug_rands import slugfy_new
from django.contrib.auth.models import User
from utils.images import resize_image # type: ignore
from utils.log import log

class PostManager(models.Manager): # type: ignore
    """Classe para substituir o objects da classe Post.
    adicionando novos metodos ao objeto 'objects"""
    @property
    def get_published(self): # type: ignore
        """Retorna os dados em que is_published = True ordenados por ID"""
        return self\
            .filter(is_published=True)\
            .order_by('-pk')

class Post(models.Model):
    """Model para os Posts"""
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    objects = PostManager()
    
    title = models.CharField(max_length=65,)
    #adicao de uma slig que é como se fosse uma url/id da Tag
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )
    excerpt = models.CharField(
        max_length=150,
        help_text='Um breve resumo do Post.')
    is_published = models.BooleanField(
        default=False,
        help_text='Este campo precisara estar marcado para o post seja exibido.'
    )
    content = models.TextField(
        help_text='Conteudo do Post'
    )
    cover = models.ImageField(
        upload_to='posts/%Y/%m/',
        blank=True,
        default='',
        help_text="Imagem a ser exibido como capa do post.",
    )
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text='Se marcado, exibira a foto da capa no post.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Data da criação. Automatico.')
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='post_created_by' #nome da query inversa para ser usada
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Data da Modificação. Automatico.'
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='post_updated_by'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    tags = models.ManyToManyField( # type: ignore
        Tag,
        blank=True,
        default=''
    )

    def save(self,*args, **kwargs): # type: ignore
        """Ao salvar, verifica que existe uma slug e caso nao tenha, cria e 
        salva o dado no model"""
        l = log(__name__)
        l.debug(f'Iniciando metodo save do model : { self.__class__.__name__} ',)
        if not self.slug:
            self.slug = slugfy_new(self.title)
        #redimencionar imagem da capa
        cover_changed = False
        current_cover_name = str(self.cover.name)
        super().save(*args, **kwargs) # type: ignore

        if self.cover:
            l.debug('Verificando se a imagem foi alterada')
            #verifica que o cover foi alterado
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            l.debug('Imagem alterada')
            l.info('Redimensionando Imagem Enviada.')
            resize_image(self.cover, 900, True,70)
            l.debug('Imagem redimensionada')
    
    def __str__(self) -> str:
        return self.title