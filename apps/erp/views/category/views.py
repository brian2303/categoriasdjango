from django.shortcuts import render,redirect

# modelos
from apps.erp.models import Category,Product

# retornar HttpResponse,JsonResponse
from django.http import JsonResponse,HttpResponse

# decoradores de login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# decorador de csrf
from django.views.decorators.csrf import csrf_exempt

# vistas basadas en clases
from django.views.generic import ListView,CreateView

# paquete para convertir de un modelo a un diccionario
from django.forms import model_to_dict

# import json
import json

# impotando formularios de mi app
from apps.erp.forms import CategoryForm

# importando el metodo que me convierte un nombre de una url en una url absoluta
from django.urls import reverse_lazy

def category_list(request):
    data = {
        'title':'Listado de categorias',
        'categories': Category.objects.all()
    }
    return render(request,'category/list.html',data)
    

"""
lista las categorias
"""
class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            cat = Category.objects.get(pk=request.POST['id'])
            data = model_to_dict(cat)
        except Exception as e :
            data['error'] = str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de categorias'
        context['create_url'] = reverse_lazy('category_create')
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Categorias'
        return context
    
""" 
Crea un formulario que servira para el regitro de una nueva categoria 
"""
class CategoryCreateView(CreateView):
    model = Category
    form_class =  CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')

    # post que recibe las diferentes solicitudes.
    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                # form = CategoryForm(request.POST)
                # son los mismos metodos get_form que el de arriba, solo lo dejo para acordarme
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e :
            data['error'] = str(e)
        return JsonResponse(data)
        
    # contexto que se envia cuando se pide la creacion de una categoria
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'add'
        return context