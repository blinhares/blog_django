from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requests:HttpRequest)->HttpResponse:
    return render(
        requests,
        'blog/pages/index.html'
    )

