from django.db import models

# from ..answer.models import Answer

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    professor_name = models.CharField(max_length=200,null=True)
    subject_name = models.CharField(max_length=200,null=True)
    # answer = models.ForeignKey(Answer, on_delete= models.CASCADE)