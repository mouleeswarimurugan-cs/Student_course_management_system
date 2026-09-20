from django.contrib import admin
from myapp.models import *
# Register your models here.


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(CourseMaterial)