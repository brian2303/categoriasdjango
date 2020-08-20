from django.shortcuts import render
from apps.erp.models import Category,Product

#vistas basadas en clases
from django.views.generic import ListView

def category_list(request):
    data = {
        'title':'Listado de categorias',
        'categories': Category.objects.all()
    }
    return render(request,'category/list.html',data)
    


class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de categorias'
        return context
    

