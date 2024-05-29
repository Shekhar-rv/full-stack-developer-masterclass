from django import forms

class ReviewForm(forms.Form):
    """
    Creates a form for users to submit reviews
    """
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(
        label='Please write your review here',
        widget=forms.Textarea(
            attrs={'class': 'myform', 'rows': 3, 'cols': 30}
        )
    )
