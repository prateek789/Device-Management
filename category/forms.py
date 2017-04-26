from django import forms
from category.models import Category

class NameField(forms.CharField):
    def clean(self, value):
        super(NameField, self).clean(value)
        try:
            Category.objects.get(name=value)
            raise forms.ValidationError("Someone is already using this name. Please pick an other.")
        except Category.DoesNotExist:
            return value

class CategoryForm(forms.Form):
    description = forms.CharField(max_length=100)
    name = NameField(max_length=30)

class OwnerForm(forms.Form):
    ownership = forms.CharField(max_length=100)
       
