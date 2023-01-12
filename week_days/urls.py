from django.urls import path
from . import views

urlpatterns = [
    path('<day_of_the_week>/', views.tasks_for_the_day)
]
