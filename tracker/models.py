from django.db import models


# Create your models here.

class MeetingModel(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    author_id = models.CharField(max_length=100)
