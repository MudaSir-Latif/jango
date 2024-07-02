from django import forms
from about.models import CartItem, Size, Colour

class CartItemForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=Size.objects.none(), required=True)
    colour = forms.ModelChoiceField(queryset=Colour.objects.none(), required=True)

    class Meta:
        model = CartItem
        fields = ['quantity', 'size', 'colour']

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)
        if product:
            self.fields['size'].queryset = Size.objects.filter(product=product)
            self.fields['colour'].queryset = Colour.objects.filter(product=product)
class AddToCartForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=Size.objects.all())
    colour = forms.ModelChoiceField(queryset=Colour.objects.all())
    quantity = forms.IntegerField(min_value=1,max_value=3)

    class Meta:
        model = CartItem
        fields = ['size', 'colour', 'quantity']