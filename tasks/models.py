from django.db import models
from utils.models import Timestamps
from django.contrib.auth import get_user_model

# Create your models here.


class Task(Timestamps, models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.title


