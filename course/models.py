from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()
    description = models.TextField(blank = True, null=True)


    def __str__(self):
        return f'{self.name} course --'