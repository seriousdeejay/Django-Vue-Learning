from django.db import models
from utils.models import Timestamps
from django.contrib.auth import get_user_model

# Create your models here.


class List(Timestamps, models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # get_user_model() --> https://www.youtube.com/watch?v=VvySuG0zk2E&list=PLFBirL3MAv2-TBWLoBXF8gyykAHvZg_1B&index=3 27:00
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=1000, null=True)

	def __str__(self):
		return self.name


class ListItem(Timestamps, models.Model):
	parent_list = models.ForeignKey(List, on_delete=models.CASCADE)
	text = models.CharField(max_length=255)

	def __str__(self):
		return self.text
