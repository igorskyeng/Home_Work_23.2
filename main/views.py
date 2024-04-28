from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from main.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name} ({email})')
    return render(request, 'main/contacts.html')


class ContactPageView(TemplateView):
    template_name = "main/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def home(request):
    return render(request, 'main/home.html')


class ProductDetailtView(DetailView):
    model = Product
    template_name = 'main/index.html'
