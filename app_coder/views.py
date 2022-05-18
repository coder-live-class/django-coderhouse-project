from django.shortcuts import render

from app_coder.models import Course, Student, Profesor, Homework


def index(request):
    return render(request, "app_coder/index.html")


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


def post_course(request, name: str, code: int):
    course = Course(name=name, code=code)
    course.save() # save into the DB

    context_dict = {
        'course': course
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/post_course.html"
    )


def all_courses(request):
    courses = Course.objects.all()

    context_dict = {
        'courses': courses
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/all_courses.html"
    )


def get_course(request, id):
    course = Course.objects.get(pk=id)

    context_dict = {
        'course': course
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/get_course.html",
    )
