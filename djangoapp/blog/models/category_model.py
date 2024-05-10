from django.db import models
from utils.slug_rands import slugfy_new

class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    name = models.CharField(
        max_length=255
    )
    #adicao de uma slig que é como se fosse uma url/id da Tag
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )

    def save(self,*args, **kwargs): # type: ignore
        """Ao salvar, verifica que existe uma slug e caso nao tenha, cria e 
        salva o dado no model"""
        if not self.slug:
            self.slug = slugfy_new(self.name)

        return super().save(*args, **kwargs) # type: ignore
    
    def __str__(self) -> str:
        return self.name