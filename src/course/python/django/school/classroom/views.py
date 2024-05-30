# from django.shortcuts import render
# from django.http import HttpRequest
from typing import Any
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    FormView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from classroom.forms import ContactForm
from classroom.models import Teacher


# Create your views here.
class HomeView(TemplateView):
    """Home view."""
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    """Thank you view."""
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    """Teacher create view."""
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you') # Actual URL

class TeacherListView(ListView):
    """Teacher list view."""
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = 'teacher_list'

class TeacherDetailView(DetailView):
    """Teacher detail view."""
    model = Teacher

class TeacherUpdateView(UpdateView):
    """Teacher update view share the teacher_model.html template."""
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:teacher_list') # Actual URL

class TeacherDeleteView(DeleteView):
    """Teacher delete view."""
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list') # Actual URL

class ContactFormView(FormView): # type: ignore
    """Contact form view."""
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = '/classroom/thank_you/' # Actual URL

    def form_valid(self, form: Any) -> HttpResponse:
        print(form.cleaned_data)
        return super().form_valid(form) # type: ignore
