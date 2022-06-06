from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()

    def __str__(self):
        return f'{self.name} course --'