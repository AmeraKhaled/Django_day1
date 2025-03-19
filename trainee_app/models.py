from django.db import models
from course_app.models import Course  

class Trainee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    
 
    course = models.ForeignKey('course_app.Course', on_delete=models.SET_NULL, null=True, blank=True) 

    def __str__(self):
        return self.name
