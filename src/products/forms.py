from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured',
        ]

class ProductRawForm(forms.Form):
    # title = forms.CharField()
    # description = forms.CharField()
    # price = forms.DecimalField()
    # summary = forms.CharField()
    # featured = forms.BooleanField()

    title = forms.CharField(
                        label='', 
                        widget=forms.TextInput(
                            attrs= {
                                "placeholder": "Your title"
                            }
                        )
                    )
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "rows": 10,
                                "cols": 20
                            }
                        )
                    )
    price = forms.DecimalField(initial=12.99)
    summary = forms.CharField()
    featured = forms.BooleanField()