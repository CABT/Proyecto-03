from django.db import models
from registro.models import RegistroUsuario

# Create your models here.
class Perfil(models.Model):
	usuario = models.ForeignKey(RegistroUsuario)

	def user(self):
		return self.RegistroUsuario.username 

	def __str__(self):
		return self.RegistroUsuario.username

	def __unicode__(self):
		return self.RegistroUsuario.username