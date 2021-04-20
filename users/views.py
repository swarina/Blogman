from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'