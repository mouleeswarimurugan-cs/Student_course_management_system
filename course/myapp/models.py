from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    profile_image = models.ImageField(upload_to="images/")
    resume=models.FileField(upload_to="file/")

    def __str__(self):
        return f"{self.name}"



class Course(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    duration=models.CharField(max_length=20)
    fees=models.IntegerField()
    cou_image=models.ImageField(upload_to="cou_image")

    def __str__(self):
        return f"{self.name}"




status=[
    ("Active","active"),
    ("Completed","completed"),
    ("Pending","pending")
]
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=20,choices=status)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student}"

class Instructor(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField()
    specialization = models.CharField(max_length=20)
    profile_img = models.ImageField(upload_to="pro_img")

    def __str__(self):
        return self.name

class CourseMaterial(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    file=models.FileField(upload_to="file/")

    def __str__(self):
        return f"{self.course}"