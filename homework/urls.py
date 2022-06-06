from django.urls import path

from homework import views


app_name='homework'
urlpatterns = [
    path('homeworks', views.homeworks, name='homework-list'),
    path('homework/add', views.homework_form, name='homework-add'),
]
