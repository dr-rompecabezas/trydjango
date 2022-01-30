from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title"}))
    email       = forms.EmailField()
    description = forms.CharField(label='', required=False, widget=forms.Textarea(
        attrs={
            "placeholder": "Description",
            "class": "new-class-name another-class",
            "rows": 10,
            "cols": 30
            }
        )
    )
    price = forms.DecimalField(initial=0.99)
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
    
    # override validation
    # https://docs.djangoproject.com/en/3.2/ref/forms/validation/
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "ABC" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
    
    # more realistic example
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email
            


# Pure Django form
# https://docs.djangoproject.com/en/3.2/ref/forms/fields/


class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title"}))  # by default required=True
    description = forms.CharField(label='', required=False, widget=forms.Textarea(
        attrs={
            "placeholder": "Description",
            "class": "new-class-name another-class",
            "rows": 10,
            "cols": 30
            }
        )
    )
    price = forms.DecimalField(initial=0.99)
