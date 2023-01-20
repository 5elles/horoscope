from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi
from django.urls import reverse


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    s_rectangle = width * height
    return render(request, 'geometry/rectangle.html')


def rectangle_area(request, width: int, height: int):  # redirect, бесполезное дублирование для тренировки
    redirect_url = reverse("rectangle_area", args=(width, height))
    return HttpResponseRedirect(redirect_url)


def get_square_area(request, width: int):
    s_square = width ** 2
    return render(request, 'geometry/square.html')

def get_circle_area(request, radius: int):
    s_circle = pi * radius ** 2
    return render(request, 'geometry/circle.html')
