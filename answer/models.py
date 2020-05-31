from django.db import models

# Create your models here.
from django.db import models
from question.models import *
# Create your models here.

class Answer(models.Model): 
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    
    selected = models.BooleanField(null=False, default=False)
   
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return self.title