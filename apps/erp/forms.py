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

        """
            personalizacion de campos del modelo para mostrar en pantalla
        """
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

    """
        sobre escribiendo el metodo save de la clase ModelForm
    """
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
            
        return data