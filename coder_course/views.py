from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


from coder_course.models import Course


def post_course1(self, name: str, code: int):
    template = loader.get_template('post_course.html')

    course = Course(name=name, code=code)
    course.save() # save into the DB

    context_dict = {
        'course': course
    }

    render = template.render(context_dict)
    return HttpResponse(render)


def post_course2(request, name: str, code: int):
    course = Course(name=name, code=code)
    course.save() # save into the DB

    context_dict = {
        'course': course
    }

    return render(
        request=request,
        context=context_dict,
        template_name="coder_course/post_course.html"
    )

def all_courses1(self):
    template = loader.get_template('all_courses.html')

    courses = Course.objects.all()

    context_dict = {
        'courses': courses
    }

    render = template.render(context_dict)
    return HttpResponse(render)


def all_courses2(request):
    courses = Course.objects.all()

    context_dict = {
        'courses': courses
    }

    return render(
        request=request,
        context=context_dict,
        template_name="coder_course/all_courses.html"
    )


def get_course1(self, id: int):

    template = loader.get_template('get_course.html')

    course = Course.objects.get(pk=id)

    context_dict = {
        'course': course
    }

    render = template.render(context_dict)
    return HttpResponse(render)


def get_course2(request, id):
    course = Course.objects.get(pk=id)

    context_dict = {
        'course': course
    }

    return render(
        request=request,
        context=context_dict,
        template_name="coder_course/get_course.html",
    )


def index1(self):
    template = loader.get_template('index.html')
    render = template.render()
    return HttpResponse(render)


def index2(request):
    return render(request, "coder_course/index.html")


def cursos(request):
    return render(request, "coder_course/cursos.html")
