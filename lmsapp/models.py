
from django.db import models

class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=15)

#for quiz

class quizmodel(models.Model):
    question=models.CharField(max_length=1000)
    op1=models.CharField(max_length=1000)
    op2=models.CharField(max_length=1000)
    op3=models.CharField(max_length=1000)
    op4=models.CharField(max_length=1000)
    answer=models.CharField(max_length=1000)

    def __str__(self):
        return self.question

#for file upload 
class file_model(models.Model):
    file=models.FileField()
    class Meta:
        db_table="file_model"
