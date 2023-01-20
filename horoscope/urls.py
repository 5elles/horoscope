from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index),
    path('types', views.types),
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('types/<str:type_of_el>', views.elements, name="astro_elements"),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name="horoscope_name")
]
