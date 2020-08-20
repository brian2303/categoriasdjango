from django.urls import path
from apps.erp.views.category.views import *

urlpatterns = [
    path('category/list',CategoryListView.as_view(),name='category_list'),
]