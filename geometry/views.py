from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {width * height}")


def rectangle_area(request, width: int, height: int):   # redirect, бесполезное дублирование для тренировки
    return HttpResponseRedirect(f"/calculate_geometry/rectangle/{width}/{height}")


def get_square_area(request, width: int):
    return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {width ** 2}")


def get_circle_area(request, radius: int):
    return HttpResponse(f"Площадь круга с радиусом {radius} равна {pi * radius ** 2}")
