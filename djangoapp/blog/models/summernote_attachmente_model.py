from django_summernote.models import AbstractAttachment # type: ignore
from utils.images import resize_image # type: ignore
from utils.log import log

class PostAttachment(AbstractAttachment):
        """Escrevendo o Model para anexos do SummerNote"""
        
        class Meta: # type: ignore
            verbose_name = 'Anexo do Post'
            verbose_name_plural = 'Anexos dos Posts'

        def save(self, *args, **kwargs): # type: ignore
            l = log(__name__)
            l.debug(f'Iniciando metodo save do model : { self.__class__.__name__} ',)
            if not self.name:
                self.name = self.file.name

            current_file_name = str(self.file.name)
            super_save = super().save(*args, **kwargs) # type: ignore
            file_changed = False

            if self.file:
                l.debug('Verificando se a imagem foi alterada')
                file_changed = current_file_name != self.file.name

            if file_changed:
                l.debug('Imagem alterada')
                l.info('Redimensionando Imagem Enviada.')
                resize_image(self.file, 900, True, 70)
                l.debug('Imagem redimensionada')


            return super_save