# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def junuary(request):

    return HttpResponse("<h1>Eat no Meat through Junuary</h1>")
def february(request):

    return HttpResponse("<h1>walk 20 minute through february</h1>")
