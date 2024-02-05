from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SearchHistory(models.Model):
    sname = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    ipaddress = models.CharField(max_length=50)

    def __str__(self):
        return self.name    
