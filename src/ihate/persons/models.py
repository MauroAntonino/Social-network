from django.db import models


class Pessoas(models.Model):
	"""docstring for Person"""
	nome		= models.CharField(max_length=30)
	apelidio	= models.CharField(max_length=30)
	foto		= models.ImageField(upload_to='fotos/', null=True, blank=True)

	def __str(self):
		return self.nome
# Create your models here.
