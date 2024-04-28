from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse

from pytils.translit import slugify

from main.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name_product', 'Description', 'category', 'price_per_purchase', 'image_preview')
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name_product)
            new_product.save()

        return super().form_valid(form)


class ProductListView(ListView):
    model = Product


class ProductDetailtView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name_product', 'Description', 'category', 'price_per_purchase', 'image_preview')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name_product)
            new_product.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:view_product', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:index')


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
