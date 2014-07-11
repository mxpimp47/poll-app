from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from newsletter.models import NewsLetter

class NewsLetterView(generic.NewsLetterView):
    model = NewsLetter
    template_name = 'newsletter/signup.html'