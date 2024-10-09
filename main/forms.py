from django import forms
from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "category", "image", "rating"]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'min': 0}),
        }
    def clean_name(self):
            name = self.cleaned_data.get('name')
            return strip_tags(name)  # Remove any HTML tags

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return strip_tags(description)  # Remove any HTML tags

    def clean_category(self):
        category = self.cleaned_data.get('category')
        return strip_tags(category)  # Remove any HTML tags