from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic.base import TemplateView


def index(request):
    return HttpResponse("Placeholder Entry")


class HomepageDefaultView1(TemplateView):
    template_name = 'homepage.html'
