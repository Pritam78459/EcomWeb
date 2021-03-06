from django.urls import path
from .views import (

		ProductListView, 
		ProductDetailView, 
		ProductCreateView, 
		ProductUpdateView,
		ProductDeleteView,
		cart,
		checkout,

)
from . import views

urlpatterns = [
	path('', ProductListView.as_view(), name='shop-home'),
	path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
	path('about/', views.about, name='shop-about'),
	path('cart/', cart, name='shop-cart'),
	path('checkout/', checkout, name='shop-checkout'),
	path('product/new/', ProductCreateView.as_view(), name='product-create'),
	path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
	path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
	path('update_item/', views.updateItem, name='update_item'),
	

]


