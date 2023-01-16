from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('types', views.types),
    path('types/<str:type_of_el>', views.elements, name="astro_elements"),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name="horoscope_name")
]
