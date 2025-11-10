# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
challenges_month = {
    "january": "Learn to code",
    "february": "Learn django",
    "march": "Learn to code and django",
    "april": "Learn ai and machine learning",
    "may": "Learn react and angular",
    "june": "Learn web development",
    "july": "Learn deep learning",
    "august": "Learn frontend and backend",
    "september": "Learn clean code",
    "october": "Learn review code",
    "november": "Learn python and javascript",
    "december": "Learn to develop mobile app and web app with flutter and react native",
}


# def february(reqest):
#     return HttpResponse(challenges_month["february"])
# def january(reqest):
#     return HttpResponse(challenges_month["january"])

def monthly_challenges(reqest, month):
    if month not in challenges_month:
        return HttpResponse("This month is not supported")
    return HttpResponse(challenges_month[month])
