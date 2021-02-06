from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
			ListView, 
			DetailView, 
			CreateView, 
			UpdateView,
			DeleteView,
	)
from .models import Product


def home(request):
	context = {
		'products' : Product.objects.all(),
		
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
	return render(request, 'shop/about.html',{'title' : 'About'})

