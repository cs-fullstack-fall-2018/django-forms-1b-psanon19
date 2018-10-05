from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    confirm = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    url = forms.CharField(widget=forms.URLInput)
