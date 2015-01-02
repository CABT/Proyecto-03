from django.forms import ModelForm

from . import models

class HiloForma(ModelForm):
    class Meta:
        model = models.Hilo
        fields = ["titulo", "contenido"]
        
        def save(self, commit =True ):
            hilo = super(HiloForma,self).save(commit=False)
            hilo.titulo = self.cleaned_data['titulo']
            hilo.contenido = self.cleaned_data['contenido']
            if commit:
                hilo.save()
            return hilo


class ComentarioForma(ModelForm):
    class Meta:
        model = models.Comentario
        fields = ["contenido"]
        
        def save(self, commit=True):
            comentario = super(Comentario, self).save(commit=False)
            comentario.contenido = self.cleanes_data['contenido']
            if commit:
                comentario.save()
            return comentario
        
