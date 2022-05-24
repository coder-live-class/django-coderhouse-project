from django.urls import path

from app_coder import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('profesors', views.profesors, name='Profesors'),
    path('courses', views.courses, name='Courses'),
    path('students', views.students, name='Students'),
    path('homeworks', views.homeworks, name='Homeworks'),
    path('formHTML', views.form_hmtl),
    path('course-django-forms', views.course_forms_django, name='CourseDjangoForms'),
    path('profesor-django-forms', views.profesor_forms_django, name='ProfesorDjangoForms'),
    path('homework-django-forms', views.homework_forms_django, name='HomeworkDjangoForms'),
    path('search', views.search, name='Search'),
]
