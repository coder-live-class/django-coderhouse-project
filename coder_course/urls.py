from django.urls import path

from coder_course import views

urlpatterns = [
    path('index-1', views.index1),
    path('get-course-1/<int:id>/', views.get_course1),
    path('post-course-1/<str:name>/<int:code>/', views.post_course1),
    path('all-courses-1/', views.all_courses1),

    path('index-2', views.index2),
    path('get-course-2/<int:id>/', views.get_course2),
    path('post-course-2/<str:name>/<int:code>/', views.post_course2),
    path('all-courses-2/', views.all_courses2),

    path('cursos', views.cursos),
]