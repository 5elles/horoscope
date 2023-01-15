from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
dct = {
    'monday': 'в понедельник я жалею себя',
    'tuesday': 'во вторник - глазею в пропасть',
    'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
    'thursday': 'в четверг - зарядка',
    'friday': 'ужин с собой, нельзя снова его пропускать',
    'saturday': 'в субботу - борьба с презрением к себе',
    'sunday': 'в воскресенье - иду на рождество'
}


def get_tasks(request, day_of_the_week: str):
    if day_of_the_week in dct:
        return HttpResponse(dct[day_of_the_week])
    else:
        return HttpResponseNotFound(f"В следующий раз хорошо подумай, прежде чем вводить это - '{day_of_the_week}'")


def get_tasks_withDayNumber(request, day_of_the_week: int):
    if day_of_the_week < 1 or day_of_the_week > 7:
        return HttpResponse(f"Неверный номер дня - {day_of_the_week}")
    else:
        dayNumber = list(dct)[day_of_the_week - 1]
        redirect_url = reverse("todo_week_url", args=(dayNumber,))
        return HttpResponseRedirect(redirect_url)
