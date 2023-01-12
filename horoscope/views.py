from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def get_info_about_sign_zodiac(request, sign_zodiac):
    if sign_zodiac == 'aries':
        return HttpResponse("Aries [ɛəri:z] / Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")

    elif sign_zodiac == 'gemini':
        return HttpResponse("Gemini ['dʒeminai] / Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")

    elif sign_zodiac == 'cancer':
        return HttpResponse("Cancer ['kænsə(r)] / Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).")

    elif sign_zodiac == 'leo':
        return HttpResponse("Leo ['li:əu] / Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).")

    elif sign_zodiac == 'virgo':
        return HttpResponse("Virgo ['vз:gəu] / Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).")

    elif sign_zodiac == 'libra':
        return HttpResponse("Libra ['li:brə] / Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).")

    elif sign_zodiac == 'scorpio':
        return HttpResponse("Scorpio ['skɔ:piəu] / Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).")

    elif sign_zodiac == 'sagittarius':
        return HttpResponse("Sagittarius [sædʒi'tɛəriəs] / Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).")

    elif sign_zodiac == 'capricorn':
        return HttpResponse("Capricorn ['kæprikɔ:n] / Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).")

    elif sign_zodiac == 'aquarius':
        return HttpResponse("Aquarius [ə'kwɛəriəs] / Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).")

    elif sign_zodiac == 'pisces':
        return HttpResponse("Pisces ['paisi:z] / Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).")

    elif sign_zodiac == 'taurus':
        return HttpResponse("Taurus ['tɔ:rəs] / Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")

    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")

