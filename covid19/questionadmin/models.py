from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField(blank=True, null=True)


class Location(models.Model):
    name = models.TextField(blank=True)


class Participant(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    location = models.ForeignKey('Location', models.DO_NOTHING)


class Answer(models.Model):
    question = models.ForeignKey('Question', models.DO_NOTHING)
    participant = models.ForeignKey('Participant', models.DO_NOTHING)
    scale_Answer = models.IntegerField()
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()
    freeform_text = models.TextField()
