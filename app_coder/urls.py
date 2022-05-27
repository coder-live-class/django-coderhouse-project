from django.urls import path

from app_coder import views

app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
    path('profesors', views.profesors, name='Profesors'),
    # path('courses', views.courses, name='course-list'),
    path('students', views.students, name='Students'),
    path('homeworks', views.homeworks, name='Homeworks'),
    path('formHTML', views.form_hmtl),
    path('course-django-forms', views.course_forms_django, name='CourseDjangoForms'),
    path('profesor-django-forms', views.profesor_forms_django, name='ProfesorDjangoForms'),
    path('profesor/<int:pk>/update', views.update_profesor, name='UpdateProfesor'),
    path('profesor/<int:pk>/delete', views.delete_profesor, name='DeleteProfesor'),
    path('homework-django-forms', views.homework_forms_django, name='HomeworkDjangoForms'),
    path('search', views.search, name='Search'),


    # Dajngo documentation -->  https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    # Confirmo la url de la documentación es correcta, deben hacer scroll hasta esta parte:
    #
    # from django.urls import path
    # from myapp.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView

    # urlpatterns = [
    #     # ...
    #     path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    #     path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    #     path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    # ]
    #
    # Acá se ve la forma clara cómo Django realiza de forma stándar los nombres para urls, views y name del path.

    path('courses', views.CourseListView.as_view(), name='course-list'),
    path('course/add/', views.CourseCreateView.as_view(), name='course-add'),
    path('course/<int:pk>/detail', views.CourseDetailView.as_view(), name='course-detail'),
    path('course/<int:pk>/update', views.CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete', views.CourseDeleteView.as_view(), name='course-delete'),
]
