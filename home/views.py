from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.shortcuts import render
from .models import HomePage, Testtt, Test, CustomText, Testing


def home(request):
    packages = [
        {"name": "stripe", "url": "http://pypi.python.org/pypi/stripe/1.77.1"},
        {"name": "boto3", "url": "http://pypi.python.org/pypi/boto3/1.5.15"},
        {
            "name": "django-allauth",
            "url": "https://pypi.org/project/django-allauth/0.38.0/",
        },
        {
            "name": "django-bootstrap4",
            "url": "https://pypi.org/project/django-bootstrap4/0.0.7/",
        },
        {
            "name": "djangorestframework",
            "url": "https://pypi.org/project/djangorestframework/3.9.0/",
        },
    ]
    context = {
        "customtext": CustomText.objects.first(),
        "homepage": HomePage.objects.first(),
        "packages": packages,
    }
    return render(request, "home/index.html", context)
