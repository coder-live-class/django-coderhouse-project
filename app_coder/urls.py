from django.urls import path

from app_coder import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('profesors', views.profesors, name='Profesors'),
    path('courses', views.courses, name='Courses'),
    path('students', views.students, name='Students'),
    path('homeworks', views.homeworks, name='Homeworks'),

    path('get-course/<int:id>/', views.get_course),
    path('post-course/<str:name>/<int:code>/', views.post_course),
    path('all-courses/', views.all_courses),
]
