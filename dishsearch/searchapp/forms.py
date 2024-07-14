from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search for a dish', max_length=255)
