
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from course.models import Course

class CourseListView(ListView):
    model = Course
    template_name = "course/course_list.html"


class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course_detail.html"
    fields = ['name', 'code', 'description']


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    success_url = reverse_lazy('course:course-list')
    fields = ['name', 'code', 'description']


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    success_url = reverse_lazy('course:course-list')
    fields = ['name', 'code', 'description']


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('course:course-list')
