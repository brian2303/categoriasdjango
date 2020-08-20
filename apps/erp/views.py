from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Category,Product

# Create your views here.

# def my_first_view(request):
#     return HttpResponse('hola url')

def my_first_view(request):
    data = {
        'nombre':'brian',
        'categories': Category.objects.all()
    }
    return render(request,'home.html',data)

def second_view(request):
    data = {
        'nombre':'brian',
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request,'second.html',data)