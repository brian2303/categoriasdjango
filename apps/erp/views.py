from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
# Create your views here.

# def my_first_view(request):
#     return HttpResponse('hola url')

def my_first_view(request):
    data = {
        'nombre':'brian'
    }
    return render(request,'index.html',data)
