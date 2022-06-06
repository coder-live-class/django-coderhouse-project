from django.urls import path

from course import views


app_name='course'
urlpatterns = [
    path('courses', views.CourseListView.as_view(), name='course-list'),
    path('course/add/', views.CourseCreateView.as_view(), name='course-add'),
    path('course/<int:pk>/detail', views.CourseDetailView.as_view(), name='course-detail'),
    path('course/<int:pk>/update', views.CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete', views.CourseDeleteView.as_view(), name='course-delete'),
]
