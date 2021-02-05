from django.db import models

# Create your models here.


class Aboutme(models.Model):
    title = models.CharField(max_length=50)
    descrption = models.TextField()

    def __str__(self):
        return self.title


class Technologie(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Project(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField()
    technology = models.ManyToManyField(Technologie)
    source_code = models.URLField()
    deployed_version = models.URLField()

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Collaboration(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
