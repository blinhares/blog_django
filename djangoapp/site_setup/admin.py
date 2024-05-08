from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup
from django.http import HttpRequest

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin): # type: ignore
    list_display = 'id', 'text', 'url_or_path'
    search_fields = list_display
    list_display_links = list_display

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin): # type: ignore
    list_display = 'title', 'description',

    def has_add_permission(self, request:HttpRequest) -> bool:
        """Esse metodo reescrito de `admin.ModelAdmin`.
        Esse metodo é responsavel por mostrar o botaoo `+ Adicionar` ao model.
        Vamos desabiliatar este botal caso o model ja apresente algum dado.

        Args:
            request (HttpRequest): requisaição HTTP

        Returns:
            bool: Retorna um Bool se mostra ou nao o objeto
        """
        return not SiteSetup.objects.exists()
