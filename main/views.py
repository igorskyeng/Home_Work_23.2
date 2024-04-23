from django.shortcuts import render
from main.models import Product


def index(request):
    #object_pk = Product.objects.get(pk=pk)
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        #'object_pk': object_pk
    }
    return render(request, 'main/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name} ({email})')
    return render(request, 'main/contacts.html')


def home(request):
    return render(request, 'main/home.html')
