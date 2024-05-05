from django import forms

from main.models import Product
from main.models import Version
from blog.models import Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CleanNameProductMixin:
    def clean_name_product(self):
        cleaned_data = self.cleaned_data['name_product']
        list_banned = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for l_b in list_banned:
            if l_b in cleaned_data:
                raise forms.ValidationError('Запрещенное слово!')

        return cleaned_data


class ProductAddForm(StyleFormMixin, CleanNameProductMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name_product', 'Description', 'category', 'price_per_purchase', 'publication_sign')


class ProductForm(StyleFormMixin, CleanNameProductMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name_product', 'price_per_purchase')


class ModeratorFormProducts(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name_product', 'Description', 'category', 'price_per_purchase', 'publication_sign')


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = 'name_product', 'version_number', 'name_version', 'sign_current_version'


class BlogForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = 'title', 'body', 'image_preview'
