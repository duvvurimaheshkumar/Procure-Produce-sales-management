from django import forms


class ProducerSignUpForm(forms.Form):
    fname = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    lname = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    contact = forms.CharField(label='Contact', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    postcode = forms.CharField(label='Postal Code', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    address = forms.CharField(label='Address', max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    pictures = forms.FileField(label='Attach picture')
    document = forms.FileField(label='Attach Document')
