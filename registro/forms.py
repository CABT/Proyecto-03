# -*- coding: UTF-8 -*-
from django import forms
from .models import RegistroUsuario
from django.utils.translation import ugettext_lazy as _
import re

class FormaRegistro(forms.ModelForm):

    password = forms.CharField( 
        label='Contraseña', 
        widget=forms.PasswordInput()
    )
    password_check = forms.CharField(
        label='Ingrese su contraseña nuevamente',
        widget=forms.PasswordInput()
    )

    descripcion = forms.CharField(
        widget=forms.Textarea,
        help_text='Escribe algo sobre tí en un máximo de 255 carácteres. Campo no requerido',
        required = False
    )
    
    class Meta:
        model = RegistroUsuario
        fields = ["username", "correo", "password", 
                  "password_check", "pais", "avatar", "descripcion"]

    def clean_password_check(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password_check = self.cleaned_data['password_check']
            if password == password_check:
                return password_check
            raise forms.ValidationError('Las contraseñas no coinciden.')
            
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Usuario solo puede contener '
                                        'caracteres alfanumericos y' 
                                        'guiones bajos.')
        try:
            RegistroUsuario.objects.get(username=username)
        except RegistroUsuario.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario ya existe.')

    def clean_email(self):
        if RegistroUsuario.objects.filter(
                email__iexact=self.cleaned_data['correo']).count():
            raise forms.ValidationError(u'Este correo ya está en uso,'
                                        'por favor utilice otro.')
        return self.cleaned_data['correo']

    def save(self, commit=True):
        usuario = super(FormaRegistro, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password"])
        if commit:
            usuario.save()
        return usuario


#class FormaIniciaSesion(forms.ModelForm):
    
