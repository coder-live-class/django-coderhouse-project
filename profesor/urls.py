from django.urls import path

from profesor import views


app_name='profesor'
urlpatterns = [
    path('profesors', views.profesor_list, name='profesor-list'),
    path('profesor/add', views.profesor_form, name='profesor-add'),
    path('profesor/<int:pk>/update', views.update_profesor, name='profesor-update'),
    path('profesor/<int:pk>/delete', views.delete_profesor, name='profesor-delete'),
]
