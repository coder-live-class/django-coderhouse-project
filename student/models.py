from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'Nombre del Estudiante: {self.name} {self.last_name} -- '