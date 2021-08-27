from django.db import models

# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField()
	author = models.CharField(max_length=200)


	def __str__(self):
		return self.name