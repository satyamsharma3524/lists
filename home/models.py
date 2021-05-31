from django.db import models

# Create your models here.

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    Task_name = models.CharField(max_length=25)
    Task_desc = models.CharField(max_length=300)
    timing = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Task_name


class Contacts(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    contact = models.IntegerField()
    desc = models.CharField(max_length=250)

    def __str__(self):
        return self.name

