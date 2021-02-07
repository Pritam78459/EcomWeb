from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

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


	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'pk':self.pk})

class Customer(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
	name = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	date_orderd = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	transaction_id = models.CharField(max_length=200,null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total
	
	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True,blank=True)
	date_added= models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	address = models.CharField(max_length=200,null=True)
	city = models.CharField(max_length=200,null=True)
	state = models.CharField(max_length=200,null=True)
	zipcode = models.CharField(max_length=200,null=True)
	date_added= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
