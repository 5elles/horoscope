from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting),
    path('<int:day_of_the_week>', views.get_tasks_withDayNumber),
    path('<str:day_of_the_week>', views.get_tasks, name="todo_week_url")
]
