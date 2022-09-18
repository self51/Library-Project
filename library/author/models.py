from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name + ' ' + self.surname + ' ' + self.patronymic)