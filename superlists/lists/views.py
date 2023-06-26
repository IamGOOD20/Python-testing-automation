from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    '''home page'''
    return render(request, 'lists/home.html')
