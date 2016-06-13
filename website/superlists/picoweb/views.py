from django.shortcuts import render_to_response, redirect
from picoweb.models import Product, Photo

def index(request):
	products_list = Product.objects.all()
	return render_to_response('index.html', locals())


