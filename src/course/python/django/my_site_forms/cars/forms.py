from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     """
#     Creates a form for users to submit reviews
#     """
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(
#         label='Please write your review here',
#         widget=forms.Textarea(
#             attrs={'class': 'myform', 'rows': 3, 'cols': 30}
#         )
#     )


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'stars']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'stars': 'Rating',
        }
        error_messages = {
            'stars': {
                'min_value': 'Please enter a number between 1 and 5.',
                'max_value': 'Please enter a number between 1 and 5.',
            }
        }
