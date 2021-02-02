from django.shortcuts import render

products = [
	{
	'seller' : 'Computer Services',
	'name' : 'monitor',
	'image' : 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.zJdTTM6hqrU7I-1Yo-SRvgHaEK%26pid%3DApi&f=1',
	'date_added' : 'February 1, 2021'
	},
	{
	'seller' : 'Electronics',
	'name' : 'TV',
	'image' : 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn57.androidauthority.net%2Fwp-content%2Fuploads%2F2019%2F11%2FXiaomi-Mi-TV-4X-55-2020-Edition-920x470.jpg&f=1&nofb=1',
	'date_added' : 'January 29, 2021'
	},
	{
	'seller' : 'Electronics',
	'name' : 'TV',
	'image' : 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn57.androidauthority.net%2Fwp-content%2Fuploads%2F2019%2F11%2FXiaomi-Mi-TV-4X-55-2020-Edition-920x470.jpg&f=1&nofb=1',
	'date_added' : 'January 29, 2021'
	},
	{
	'seller' : 'Electronics',
	'name' : 'TV',
	'image' : 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn57.androidauthority.net%2Fwp-content%2Fuploads%2F2019%2F11%2FXiaomi-Mi-TV-4X-55-2020-Edition-920x470.jpg&f=1&nofb=1',
	'date_added' : 'January 29, 2021'
	},
	{
	'seller' : 'Electronics',
	'name' : 'TV',
	'image' : 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn57.androidauthority.net%2Fwp-content%2Fuploads%2F2019%2F11%2FXiaomi-Mi-TV-4X-55-2020-Edition-920x470.jpg&f=1&nofb=1',
	'date_added' : 'January 29, 2021'
	},
	{
	'seller' : 'Electronics',
	'name' : 'TV',
	'image' : 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn57.androidauthority.net%2Fwp-content%2Fuploads%2F2019%2F11%2FXiaomi-Mi-TV-4X-55-2020-Edition-920x470.jpg&f=1&nofb=1',
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