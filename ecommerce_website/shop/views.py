from django.shortcuts import render

products = [
	{
	'seller' : 'Computer Services',
	'name' : 'monitor',
	'image' : 'image link',
	'date_added' : 'February 1, 2021'
	},
	{
	'seller' : 'Electronics',
	'name' : 'TV',
	'image' : 'image link',
	'date_added' : 'January 29, 2021'
	},
]

def home(request):
	context = {
		'products' : products,
		'title' : 'Home'
	}
	return render(request, 'shop/home.html',context)


def about(request):
	return render(request, 'shop/about.html',{'title' : 'About'})