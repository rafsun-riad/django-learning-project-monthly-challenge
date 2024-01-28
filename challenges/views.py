from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges_dict = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes everyday",
    "march": "Learn Django for at least 20 minutes everyday",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes everyday",
    "june": "Learn Django for at least 20 minutes everyday",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at least 20 minutes everyday",
    "september": "Learn Django for at least 20 minutes everyday",
    "october": "Eat no meat for the entire month",
    "november": "Walk for at least 20 minutes everyday",
    "december": "Learn Django for at least 20 minutes everyday",
}


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenges_text = monthly_challenges_dict[month]
        return HttpResponse(challenges_text)
    except KeyError:
        return HttpResponseNotFound("This month is not supported")
