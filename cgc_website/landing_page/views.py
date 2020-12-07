from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello you")

    # HttpResponse("Hello you")
    return render(request, "landing_page/home.html")
