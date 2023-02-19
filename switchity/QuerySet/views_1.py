from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.Enroll import loader
from .models import Member


def testing(request):
    mydata = Member.objects.all()
    template = loader.get_template('first_template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))
