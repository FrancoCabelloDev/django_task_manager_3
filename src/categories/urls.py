from django.urls import path
from .views import category_list, category_create

urlpatterns = [
    path('', category_list, name='category_list'),  # URL base: /categories/
    path('create/', category_create, name='category_create'),  # /categories/create/
]
