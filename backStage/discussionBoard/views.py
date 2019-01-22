from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'discussionBoard/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

def index(request):
    return render(request, 'discussionBoard/index.html')

def contact(request):
    return render(request, 'discussionBoard/Contact.html')

def discussion(request):
    return render(request, 'discussionBoard/discussion.html')

def Q_A(request):
    return render(request, 'discussionBoard/QASession.html')
