
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from student.models import Student

class StudentListView(ListView):
    model = Student
    template_name = "student/student_list.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "student/student_detail.html"


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy('student:student-list')
    fields = '__all__'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    success_url = reverse_lazy('student:student-list')
    fields = '__all__'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student:student-list')
