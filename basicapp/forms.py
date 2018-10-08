from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    confirm = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    url = forms.CharField(widget=forms.URLInput)

    def clean(self):
        all_clean_data= super().clean()
        email1 = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('confirm')
        if (email1!=email2):
            print("Invalid data")
            raise forms.ValidationError('Invalid data: Emails dont Match')

        return all_clean_data
