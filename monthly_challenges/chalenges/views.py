# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def junuary(request):

    return HttpResponse("<h1>Eat no Meat through Junuary</h1>")


def february(request):

    return HttpResponse("<h1>walk 20 minute through february</h1>")


def month(request, month):
    challenge_text = {
        "january": "eat no meat",
        "february": "walk 20 minute",
    }

    if month in challenge_text:
        return HttpResponse(f"<h1 style='color:red'>{challenge_text[month]}</h1>")
    else:
        return HttpResponseNotFound("<h1>invalid month</h1>")
