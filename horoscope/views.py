from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {

    'aries': ('Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)', 'fire'),
    'taurus': ('Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).', 'taurus'),
    'gemini': ('Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).', 'air'),
    'cancer': ('Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).', 'water'),
    'leo': ('Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).', 'fire'),
    'virgo': ('Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).', 'taurus'),
    'libra': ('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).', 'air'),
    'scorpio': ('Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).', 'water'),
    'sagittarius': ('Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).', 'fire'),
    'capricorn': ('Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).', 'taurus'),
    'aquarius': ('Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).', 'air'),
    'pisces': ('Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).', 'water')

}


def index(request):
    zodiacs = list(zodiac_dict)  # список всех знаков (ключей)
    li_elements = ""  # результирующая строка для упорядоч-го списка
    for i in zodiacs:  # оборачиваем элементы списка в теги, добавляем ссылки.
        redirect_path = reverse("horoscope_name", args=(i,))
        li_elements += f"<li><a href='{redirect_path}'>{i.title()}</a></li>"
    response = f"""
    <ol>
        {li_elements}
    </ol>
    """
    return HttpResponse(response)


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
    description = zodiac_dict.get(sign_zodiac, None)  # значение по ключу из zodiac_dict
    if description:
        return HttpResponse(description[0])
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    if sign_zodiac < len(zodiac_dict) + 1 and sign_zodiac > 0:
        zodiac_name = list(zodiac_dict)[sign_zodiac - 1]  # значение знака зодиака по входящему порядковому номеру
        redirect_url = reverse("horoscope_name", args=(zodiac_name,))
        return HttpResponseRedirect(redirect_url)  # редирект
    else:
        return HttpResponse(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
