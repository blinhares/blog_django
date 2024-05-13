#type:ignore
from pathlib import Path
from django.conf import settings
from PIL import Image

def resize_image(image_django, new_width=800, optimize=True, quality=60) ->None:
    """Redimensiona imagem no endereco original da imagem, ou seja,
    dentro do caminho onde a imagem foi salva.

    Args:
        image_django (_type_): _description_
        new_width (int, optional): _description_. Defaults to 800.
        optimize (bool, optional): _description_. Defaults to True.
        quality (int, optional): _description_. Defaults to 60.

    Returns:
        Image: retorna Imagem redimensionada
    """
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size

    if original_width <= new_width:
        image_pillow.close()
        return image_pillow

    new_height = round(new_width * original_height / original_width)

    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)

    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    return new_image