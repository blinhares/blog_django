import logging
from pathlib import Path
from django.conf import settings

# formato da msg de log deve ser add como atributo format em basicConfig
# log_format = '[%(asctime)s] - %(levelname)s:%(name)s:%(message)s'

def log(
        name:str,
        log_format:str = '[%(asctime)s] - %(levelname)s:%(name)s:%(message)s'
        ) -> logging.Logger:
    
    log_path = Path(settings.MEDIA_ROOT / 'log.log')
    
    try:
        debug = settings.DEBUG
    except:
        debug = False

    if debug:
        basic_config = { # type: ignore
            'level' : logging.DEBUG,
            'format' : log_format
            }
        
    else:
        basic_config = { # type: ignore
            'filename':log_path,
            'level' : logging.INFO,#nao mostra arquivos de debug
            'format' : log_format
            }
        
    logging.basicConfig(**basic_config) # type: ignore
    return logging.getLogger(name)
