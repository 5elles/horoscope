from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.template.loader import render_to_string
from dataclasses import dataclass

# Create your views here.

zodiac_dict = {

    'aries': ('Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)', 'fire', {3: (21, 31), 4: (1, 20)}),
    'taurus': (
        'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).', 'taurus', {4: (21, 30), 5: (1, 21)}),
    'gemini': (
        'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).', 'air', {5: (22, 31), 6: (1, 21)}),
    'cancer': ('Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).', 'water', {6: (22, 30), 7: (1, 22)}),
    'leo': ('Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).', 'fire', {7: (23, 31), 8: (1, 21)}),
    'virgo': (
        'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).', 'taurus',
        {8: (22, 31), 9: (1, 23)}),
    'libra': (
        'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).', 'air',
        {9: (24, 30), 10: (1, 23)}),
    'scorpio': (
        'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).', 'water',
        {10: (24, 31), 11: (1, 22)}),
    'sagittarius': (
        'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).', 'fire',
        {11: (23, 30), 12: (1, 22)}),
    'capricorn': ('Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).', 'taurus',
                  {12: (23, 31), 1: (1, 20)}),
    'aquarius': ('Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).', 'air',
                 {1: (21, 31), 2: (1, 19)}),
    'pisces': (
        'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).', 'water',
        {2: (20, 29), 3: (1, 20)})

}


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f"Вы передали число из 4х цифр - {sign_zodiac}")


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f"Вы передали вещественное число - {sign_zodiac}")


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f"Вы передали дату - {sign_zodiac}")


def index(request):
    zodiacs = list(zodiac_dict)  # список всех знаков (ключей)
    # f"<li><a href='{redirect_path}'>{i.title()}</a></li>"
    context = {
        "zodiacs": zodiacs,
        "zodiac_dict": zodiac_dict
    }
    return render(request, "horoscope/index.html", context=context)

def types(request):
    zodiac_elements = ''
    for i in list(set(zodiac_dict[i][1] for i in zodiac_dict)):
        url_redirect = reverse("astro_elements", args=(i,))
        zodiac_elements += f"<li><a href='{url_redirect}'>{i.title()}</a></li>"
    elements_menu = f"""
    <ul>
        {zodiac_elements}
    </ul>
    """
    return HttpResponse(elements_menu)


def elements(request, type_of_el):
    signs_in_every_el = dict()  # словарь стихий и их знаков зодиака
    for i in list(set(zodiac_dict[i][1] for i in zodiac_dict)):
        signs_in_every_el[i] = list()
    for el in zodiac_dict:
        signs_in_every_el[zodiac_dict[el][1]].append(el)
    description = signs_in_every_el.get(type_of_el, None)
    if description:
        signs = ""
        for i in description:
            url_redirection = reverse(f"horoscope_name", args=(i,))
            signs += f"<li><a href = '{url_redirection}'>{i.title()}</a></li>"
        signs_menu = f"""
        <ol>
            {signs}
        </ol>
        """
        return HttpResponse(signs_menu)
    else:
        return HttpResponse(f"Нет такой стихии - '<b>{type_of_el}</b>'")


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    zodiacs = list(zodiac_dict)
    if sign_zodiac in zodiac_dict:
        data = {
            "description_zodiac": description[0],
            "sign": sign_zodiac,
            "sign_name": zodiac_dict[sign_zodiac][0].split()[0],
            "zodiacs": zodiacs,
        }
        return render(request, 'horoscope/info_zodiac.html', data)
    else:
        return render(request, 'horoscope/info_zodiac.html', None)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    if sign_zodiac < len(zodiac_dict) + 1 and sign_zodiac > 0:
        zodiac_name = list(zodiac_dict)[sign_zodiac - 1]  # значение знака зодиака по входящему порядковому номеру
        redirect_url = reverse("horoscope_name", args=(zodiac_name,))
        return HttpResponseRedirect(redirect_url)  # редирект
    else:
        return HttpResponse(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")


def get_info_by_date(request, month, day):
    days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if 0 < month < 12 and 0 < day <= days_in_month[month]:
        for i in list(zodiac_dict):
            months_in_every_sign = list(zodiac_dict[i][2])  # в каких месяцах зд присутствует
            redirect_url = reverse(f'horoscope_name', args=(i,))
            if month in months_in_every_sign:
                days_in_month = list(zodiac_dict[i][2][month])
                if day in range(days_in_month[0], days_in_month[1] + 1):
                    return HttpResponse(f"<h2>Ваш знак зодиака - {i}</h2>")
    else:
        return HttpResponseNotFound("<h2>Проверьте данные!</h2>")
