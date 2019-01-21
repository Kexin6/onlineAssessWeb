from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.http import HttpResponse


def index(request):
    template_name = 'discussionBoard/index.html'
    return HttpResponse("Hello, world. You're at the discussion board index.")
