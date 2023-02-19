from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("index")


def first_page(request):
    return render(request,'first_template.html')


def second_page(request):
    return render(request, 'second_template.html')




