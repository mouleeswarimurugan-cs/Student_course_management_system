
from django.forms import Form, ModelForm
from myapp.models import Student,Course,Instructor,CourseMaterial,Enrollment

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class InstructorForm(ModelForm):

    class Meta:
        model = Instructor
        fields = "__all__"

class MaterialForm(ModelForm):
    class Meta:
        model =CourseMaterial
        fields = "__all__"

class EnrollForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = "__all__"

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email"]