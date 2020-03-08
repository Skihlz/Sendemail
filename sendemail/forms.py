# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
	from_email = forms.EmailField(widget=forms.EmailInput(attrs={'style': 'width: 100%; color: #000000', 'placeholder': 'E-mail'}), required=True)
	name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%; color: #000000', 'placeholder': 'Name'}), required=True)
	message = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%; color: #000000', 'placeholder': 'Let us know how we can help'}), required=True)