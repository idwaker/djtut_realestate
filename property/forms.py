from django import forms


class HouseForm(forms.Form):
    title = forms.CharField(max_length=120)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=9, decimal_places=2)
    address = forms.CharField(widget=forms.Textarea)
    bedrooms = forms.IntegerField()
    bathrooms = forms.IntegerField()
    kitchens = forms.IntegerField()
