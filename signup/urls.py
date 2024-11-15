from tkinter.font import names

from django.urls import path
from .views import *
urlpatterns = [
    path('logout', log_out, name='logout'),
    path('signup', Sign_up.as_view(), name='signup')
]
