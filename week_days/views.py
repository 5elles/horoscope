from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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


def tasks_for_the_day(request, day_of_the_week):
    if day_of_the_week in dct:
        return HttpResponse(dct[day_of_the_week])
    else:
        return HttpResponseNotFound(f"В следующий раз хорошо подумай, прежде чем вводить это - '{day_of_the_week}'")
