from django.urls import path
from .views import my_first_view,second_view

urlpatterns = [
    path('uno/',my_first_view,name='vista_uno'),
    path('dos/',second_view,name='vista_dos'),
]