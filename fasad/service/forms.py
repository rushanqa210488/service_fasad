from django import forms 

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25, required=False)
    phone = forms.CharField(max_length=11)
    email = forms.EmailField(required=False)
    city = forms.CharField(max_length=50)