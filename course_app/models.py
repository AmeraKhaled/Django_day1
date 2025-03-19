from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    
    class Meta:
        db_table = "course_app_course" 

    def __str__(self):
        return self.name
