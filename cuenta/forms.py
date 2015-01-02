# -*- coding: UTF-8 -*-
from django import forms
from .models import RegistroUsuario
from django.utils.translation import ugettext_lazy as _
import re

class FormaEdicionPerfil(forms.ModelForm):
    username = forms.CharField(required=False)

    descripcion = forms.CharField(
        widget=forms.Textarea,
        help_text='Escribe algo sobre tí en un máximo de 255 carácteres. Campo no requerido',
        required = False
    )
    
    class Meta:
        model = RegistroUsuario
        fields = ["username", "correo", "pais", "avatar", "descripcion"]

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Usuario solo puede contener caracteres alfanumericos y guiones bajos.')
        try:
            nombre = RegistroUsuario.objects.get(username=username)
            #RegistroUsuario.objects.get(username=username)
        except RegistroUsuario.DoesNotExist:
            return username
        if username != self.instance.username:
                raise forms.ValidationError('Nombre de usuario ya existe.')
        else:
            return username

    def clean_email(self):
        if RegistroUsuario.objects.filter(
                email__iexact=self.cleaned_data['correo']).count():
            raise forms.ValidationError(u'Este correo ya está en uso,'
                                        'por favor utilice otro.')
        return self.cleaned_data['correo']

    def save(self, commit=True):
        usuario = super(FormaEdicionPerfil, self).save(commit=False)

        if commit:
            usuario.save()
        return usuario


#class FormaIniciaSesion(forms.ModelForm):
    
