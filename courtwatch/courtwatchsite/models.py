from django.db import models

# Create your models here.

class Story(models.Model):
	title = models.CharField(max_length=1000)
	text  = models.TextField()

