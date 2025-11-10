# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect

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

def monthly_challenge_by_number(reqest, month):
    months = list(challenges_month.keys())
    if month < 0 or month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = f"/chalenges/{redirect_month}"
    return HttpResponsePermanentRedirect(redirect_path)


def monthly_challenges(reqest, month):
    if month not in challenges_month:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenges_month[month])
