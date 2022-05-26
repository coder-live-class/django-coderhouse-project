from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

from app_coder.models import Course, Student, Profesor, Homework
from app_coder.forms import CourseForm, ProfesorForm, HomeworkForm


def index(request):
    return render(request, "app_coder/home.html")


def profesors(request):
    profesors = Profesor.objects.all()

    context_dict = {
        'profesors': profesors
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/profesors.html"
    )


def courses(request):
    courses = Course.objects.all()

    context_dict = {
        'courses': courses
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/courses.html"
    )


def students(request):
    students = Student.objects.all()

    context_dict = {
        'students': students
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/students.html"
    )


def homeworks(request):
    homeworks = Homework.objects.all()

    context_dict = {
        'homeworks': homeworks
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/homeworks.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        course = Course(name=request.POST['name'], code=request.POST['code'])
        course.save()

        courses = Course.objects.all()
        context_dict = {
            'courses': courses
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/courses.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def course_forms_django(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            course = Course(name=data['name'], code=data['code'])
            course.save()

            courses = Course.objects.all()
            context_dict = {
                'courses': courses
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/courses.html"
            )

    course_form = CourseForm(request.POST)
    context_dict = {
        'course_form': course_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/course_django_forms.html'
    )


def profesor_forms_django(request):
    if request.method == 'POST':
        profesor_form = ProfesorForm(request.POST)
        if profesor_form.is_valid():
            data = profesor_form.cleaned_data
            profesor = Profesor(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                profession=data['profession'],
            )
            profesor.save()

            profesors = Profesor.objects.all()
            context_dict = {
                'profesors': profesors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/profesors.html"
            )

    profesor_form = ProfesorForm(request.POST)
    context_dict = {
        'profesor_form': profesor_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/profesor_django_forms.html'
    )

def update_profesor(request, pk: int):
    profesor = Profesor.objects.get(pk=pk)

    if request.method == 'POST':
        profesor_form = ProfesorForm(request.POST)
        if profesor_form.is_valid():
            data = profesor_form.cleaned_data
            profesor.name = data['name']
            profesor.last_name = data['last_name']
            profesor.email = data['email']
            profesor.profession = data['profession']
            profesor.save()

            profesors = Profesor.objects.all()
            context_dict = {
                'profesors': profesors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/profesors.html"
            )

    profesor_form = ProfesorForm(model_to_dict(profesor))
    context_dict = {
        'profesor': profesor,
        'profesor_form': profesor_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/profesor_form.html'
    )


def delete_profesor(request, pk: int):
    profesor = Profesor.objects.get(pk=pk)
    if request.method == 'POST':
        profesor.delete()

        profesors = Profesor.objects.all()
        context_dict = {
            'profesors': profesors
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/profesors.html"
        )

    context_dict = {
        'profesor': profesor,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/profesor_confirm_delete.html'
    )


def homework_forms_django(request):
    if request.method == 'POST':
        homework_form = HomeworkForm(request.POST)
        if homework_form.is_valid():
            data = homework_form.cleaned_data
            homework = Homework(
                name=data['name'],
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            homework.save()

            homeworks = Homework.objects.all()
            context_dict = {
                'homeworks': homeworks
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/homeworks.html"
            )

    homework_form = HomeworkForm(request.POST)
    context_dict = {
        'homework_form': homework_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/homework_django_forms.html'
    )


def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        courses = Course.objects.filter(name__contains=search_param)
        context_dict = {
            'courses': courses
        }
    elif request.GET['code_search']:
        search_param = request.GET['code_search']
        courses = Course.objects.filter(code__contains=search_param)
        context_dict = {
            'courses': courses
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        courses = Course.objects.filter(query)
        context_dict = {
            'courses': courses
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseListView(ListView):
    model = Course
    template_name = "app_coder/course_list.html"


class CourseDetailView(DetailView):
    model = Course
    template_name = "app_coder/course_detail.html"


class CourseCreateView(CreateView):
    model = Course
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')
    fields = ['name', 'code']


class CourseUpdateView(UpdateView):
    model = Course
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')
    fields = ['name', 'code']


class CourseDeleteView(DeleteView):
    model = Course
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')
