from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from .forms import ReviewForm

# Create your views here.
def rental_review(request: HttpRequest):
    """
    View to handle the rental review form.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thank_you'))
    else:
        form = ReviewForm()
    return render(request, 'cars/rental_review.html', context={'form': form})

def thank_you(request: HttpRequest):
    """
    View to display a thank you message.
    """
    return render(request, 'cars/thank_you.html')
