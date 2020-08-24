from django.forms import *
from apps.erp.models import Category

class CategoryForm(ModelForm):

    """ 
    aplicandole a cada componente la clase form-control y autocomplete en off    
    """
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        # aplicando propiedad solo a un componente especifico
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'

        # personalizando el campo name del modelo
        widgets = {
            'name' : TextInput(
                attrs = {
                    'placeholder' : 'Ingrese un nombre...',
                }
            ),
            'desc' : Textarea(
                attrs = {
                    'placeholder':'Descripcion opcional...',
                    'rows':2,
                }
            )
        }