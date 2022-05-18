from datetime import datetime
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

from coder_course.models import Course

def template_using_context(
    self, name: str = 'Name', last_name: str = 'Last_name'):

    miHtml = open("/home/jfpinedap/coderhouse/class_18_Django_II/live_class/live_class/templates/template.html")
    template = Template(miHtml.read())
    miHtml.close()

    context_dict = {
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'my_grades': [1, 5, 6, 7, 9],
    }

    my_context = Context(context_dict)
    render = template.render(my_context)
    return HttpResponse(render)

def template_using_loader(
    self, name: str = 'Name', last_name: str = 'Last_name'):

    template = loader.get_template('template_loader.html')

    context_dict = {
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'my_grades': [1, 5, 6, 7, 9],
    }
    render = template.render(context_dict)
    return HttpResponse(render)

def post_course(
    self, name: str = 'course', code: int = 0):

    template = loader.get_template('post_course.html')

    course = Course(name=name, code=code)
    course.save() # save into the DB

    context_dict = {
        'course': course
    }

    render = template.render(context_dict)
    return HttpResponse(render)

def all_courses(self):

    template = loader.get_template('all_courses.html')

    courses = Course.objects.all()

    print('courses', type(courses), '\n', courses)
    context_dict = {
        'courses': courses
    }

    render = template.render(context_dict)
    return HttpResponse(render)

def get_course(self, id: int):

    template = loader.get_template('get_course.html')

    course = Course.objects.get(pk=id)

    context_dict = {
        'course': course
    }

    render = template.render(context_dict)
    return HttpResponse(render)

def get_course(self, id: int):

    template = loader.get_template('get_course.html')

    course = Course.objects.get(pk=id)

    context_dict = {
        'course': course
    }

    render = template.render(context_dict)
    return HttpResponse(render)

def index(self):
    template = loader.get_template('index.html')
    render = template.render()
    return HttpResponse(render)
