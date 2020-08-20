from django.urls import path
from .views import my_first_view

urlpatterns = [
    path('uno/',my_first_view),
    path('dos/',my_first_view),
]