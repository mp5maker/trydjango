from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Title"
            }
        )
    )
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured',
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "Photon" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
    
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("This is not a valid number")
        return price


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
                                "id": "my-id-for-textarea",
                                "rows": 10,
                                "cols": 20
                            }
                        )
                    )
    price = forms.DecimalField(initial=12.99)
    summary = forms.CharField()
    featured = forms.BooleanField()