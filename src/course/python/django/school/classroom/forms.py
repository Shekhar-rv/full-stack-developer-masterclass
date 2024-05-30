from django import forms


class ContactForm(forms.Form):
    """Contact form."""
    name = forms.CharField(label='Name', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)