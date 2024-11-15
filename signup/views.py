from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
def log_out(request):
    logout(request)
    return render(request,'registration/logged_out.html')

class Sign_up(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'