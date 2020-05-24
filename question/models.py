from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    pup_date = models.DateTimeField()
    body = models.TextField()


