from django.db import models
from utils.model_validator import validate_png
from utils.images import resize_image

class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    site_setup = models.ForeignKey(
        'SiteSetup',
        on_delete=models.CASCADE,#quando deletado, apagada todos os links com referencia
        blank=True,#permite valores em branco
        null=True,#permite valores nulos
        default=None,

    )
    def __str__(self):
        return self.text
    
class SiteSetup(models.Model):
    """Cria Tabelas com Dados a serem inseridos para a COnfiguracao do Site """
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    title = models.CharField(
        max_length=65,
        help_text="Titulo do Site com no máximo 65 caracteres.",
        )
    
    description = models.CharField(
        max_length=255,
        help_text="Descricao do Site com no máximo 255 caracteres.",
        )

    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True,
        default='',
        validators=[validate_png],
        help_text="Icone a ser exibido na abado navegador.",
    )

    def save(self, *args, **kwargs): # type: ignore
        """
        Sobrescreve o metodo Save do modelo herdado,
        vrifica se o faviicon foi alterado e , em caso de que sim,
        o favicon é redimensionado.

        """
        favicon_changed = False
        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs) # type: ignore

        if self.favicon:
            #verifica que o favicon foi alterado
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            resize_image(self.favicon, 32)

    def __str__(self):
        return self.title