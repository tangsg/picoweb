from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from picoweb.models import Product, Photo, Download, Feedback


def index(request):
    product_list = Product.objects.all()
    # print product_list
    return render(request, 'index.html', {'product_list': product_list})


@csrf_exempt
def proc_feedback(request):
    new_name = request.POST['name2']
    new_email = request.POST['email2']
    new_message = request.POST['message2']
    Feedback.objects.create(name=new_name, email=new_email, message=new_message)
    return HttpResponse("OK")