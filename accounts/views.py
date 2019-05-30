from django.contrib import messages

from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import Http404
from django.views import generic
from django.views.generic import CreateView

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
