from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.forms import model_to_dict
import json
from apps.erp.forms import CategoryForm
from django.urls import reverse_lazy

# modelos
from apps.erp.models import Category,Product

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
        
    # contexto que se envia cuando se pide la creacion de una categoria GET
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'add'
        return context


"""
Vista que procesara la actualización de un registro
"""
class CategoryUpdateView(UpdateView):
    """ parametros de configuracion inicial"""
    model = Category
    form_class =  CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')


    def dispatch(self, request, *args, **kwargs):
        """ asignamos el objeto que viene segun el id a la variable object """
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                # form = CategoryForm(request.POST)
                # son los mismos metodos get_form que el de arriba, solo lo dejo para acordarme
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e :
            data['error'] = str(e)
        return JsonResponse(data)


    """ entregando el contexto """
    def get_context_data(self, **kwargs):
        # print(self.object)
        # import pdb; pdb.set_trace()
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'edit'
        return context

"""eliminar una categoria"""
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/delete.html"
    success_url = reverse_lazy('category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)



    def post(self,request,*args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Eliminacion de una categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        return context
    
