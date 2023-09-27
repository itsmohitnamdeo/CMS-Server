from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    description = models.TextField()

class CourseInstance(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

