# Create your views here.
# home_page = None
from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')
