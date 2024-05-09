from typing import Any
from django.core.exceptions import ValidationError

def validate_png(image:Any)->None:
    if not image.name.lower().endswith('.png'):
        raise ValidationError('Imagem precisa estar no formato .png!')
    

