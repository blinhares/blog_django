#esse arquivo sera carregada no settings.py do projeto.
from site_setup.models import SiteSetup
from django.http import HttpRequest

def site_setup(request:HttpRequest):
    data = SiteSetup.objects.order_by('-id').first()
    return {
        'site_setup':data
            }
    
