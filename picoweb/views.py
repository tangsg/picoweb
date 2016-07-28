from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from picoweb.models import Product, Photo, Download, Feedback


def eng_or_chs(request):
    return redirect('/en/')


def index(request):
    # product_list = Product.objects.all()
    # print product_list
    return render_to_response('index.html')


def product(request, model):
    print model
    return render_to_response('product.html', {'model': model})


def about(request):
    return render_to_response('about.html')


@csrf_exempt
def proc_feedback(request):
    new_name = request.POST['name2']
    new_email = request.POST['email2']
    new_message = request.POST['message2']
    Feedback.objects.create(name=new_name, email=new_email, message=new_message)
    return HttpResponse("OK")