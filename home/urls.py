from django.urls import path

from home import views

app_name='home'
urlpatterns = [
    path('', views.index, name='main'),
    path('search', views.search, name='search'),
]
