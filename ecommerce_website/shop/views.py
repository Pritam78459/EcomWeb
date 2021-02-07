from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
			ListView, 
			DetailView, 
			CreateView, 
			UpdateView,
			DeleteView,
	)
from .models import Product, Order, OrderItem, ShippingAddress, Customer
import json


def home(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']

	context = {
		'products' : Product.objects.all(),
		'cartItems' : cartItems,
		
	}
	return render(request, 'shop/home.html',context)

class ProductListView(ListView):
	model = Product
	template_name = 'shop/home.html'
	context_object_name = 'products'
	ordering = ['-date_posted']

class ProductDetailView(DetailView):
	model = Product

class ProductCreateView(LoginRequiredMixin ,CreateView):
	model = Product
	fields = ['name','description','date_posted','price','category','image']

	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
	model = Product
	fields = ['name','description','date_posted','price','category','image']

	def form_valid(self, form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

	def test_func(self):
		product = self.get_object()
		if self.request.user == product.seller:
			return True
		return False

class ProductDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
	model = Product

	success_url = '/'

	def test_func(self):
		product = self.get_object()
		if self.request.user == product.seller:
			return True
		return False

def about(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order[get_cart_items]

	context = {'items':items, 'order':order,'cartItems':cartItems}

	return render(request, 'shop/about.html',context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order[get_cart_items]

	context = {'items':items, 'order':order,'cartItems':cartItems}
	return render(request, 'shop/cart.html',context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order[get_cart_items]
		
	context = {'items':items, 'order':order,'cartItems':cartItems}

	return render(request,'shop/checkout.html',context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action: ',action)
	print('productId: ',productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == "add":
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)