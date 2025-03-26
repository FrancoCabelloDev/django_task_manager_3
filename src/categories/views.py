from django.shortcuts import render, get_object_or_404, redirect
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Category.objects.create(name=name, description=description)
        return redirect('category_list')
    return render(request, 'categories/category_form.html')
