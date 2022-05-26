from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()

    def __str__(self):
        return f'{self.name} course --'


class Student(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'Nombre del Estudiante: {self.name} {self.last_name} -- e-mail: {self.email}'


class Profesor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre del Profesor: {self.name} {self.last_name} -- e-mail: {self.email} -- profesión: {self.profession} --'


class Homework(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()

    def __str__(self):
        is_delivered = 'Si' if self.is_delivered else 'No'
        return f'Nombre de la Entrega: {self.name} -- Fecha de entrega: {self.due_date} -- Entregado: {is_delivered}'
