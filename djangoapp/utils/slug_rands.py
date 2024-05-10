from random import SystemRandom
import string
from django.utils.text import slugify

def randon_letters(k:int=4)->str:
    """Gera letras e numeros aleatorios com o tamanho de K"""
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))

def slugfy_new(text:str, k:int=4)->str:
    """Tranforma a tag em letras e numeros e adiciona k letras e numeros
    gerados randomicamente.
    """
    return slugify(text) + '-' + randon_letters(k)
 