from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	price = models.IntegerField()
	category = models.CharField(max_length=100)
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png',upload_to='product_pics')

	def __str__(self):
		return self.name