from django.urls import path

from student import views


app_name='student'
urlpatterns = [
    path('students', views.StudentListView.as_view(), name='student-list'),
    path('student/add/', views.StudentCreateView.as_view(), name='student-add'),
    path('student/<int:pk>/detail', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/<int:pk>/update', views.StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete', views.StudentDeleteView.as_view(), name='student-delete'),
]
