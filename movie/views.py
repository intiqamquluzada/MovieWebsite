from django.shortcuts import render
from .models import Movie


def home_view(request):
    context = {}
    movies = Movie.objects.order_by("-created_at")
    context["movies"] = movies
    return render(request, "index.html", context)
