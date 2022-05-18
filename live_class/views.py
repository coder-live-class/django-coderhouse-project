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


def index(self):
    template = loader.get_template('index.html')
    render = template.render()
    return HttpResponse(render)
