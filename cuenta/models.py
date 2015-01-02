from django.db import models
from registro.models import RegistroUsuario

# Create your models here.
class Perfil(models.Model):
	usuario = models.ForeignKey(RegistroUsuario)

	def user(self):
		return self.usuario

	def __str__(self):
		return self.usuario.pk

	def __unicode__(self):
		return self.usuario.pk