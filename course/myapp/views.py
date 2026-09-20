


from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.forms import *
from myapp.models import *
from django.db.models import Q,Count

def base(request):
    return render(request,"base.html")

def student_list(request):

    search = request.GET.get("search")
    order = request.GET.get("order")
    students = Student.objects.all()
    if search:
        students = Student.objects.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search)
        )
    if order == "asc":
        students = students.order_by("name")
    elif order == "desc":
        students = students.order_by("-name")
        

    return render(request, "stu_list.html", {
        "students": students
    })


def add_student(request):
    form = StudentForm()
    students = Student.objects.all()

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    return render(request, "stu_form.html", {"form": form,"data": students})

def student_detail(request, id):
    student = Student.objects.get(id=id)

    return render(request, "stu_details.html", {
        "student": student
    })


def student_update(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(request, "stu_form.html", {
        "form": form
    })

def student_delete(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "stu_delete.html", {
        "student": student
    })


#cousrse

def course_list(request):

    courses = Course.objects.all()

    search = request.GET.get('search', '')
    duration = request.GET.get('duration', '')
    min_fees = request.GET.get('min_fees', '')
    max_fees = request.GET.get('max_fees', '')
    order = request.GET.get('order', '')

    # Search
    if search:
        courses = courses.filter(
            name__icontains=search
        )

    # Duration Filter
    if duration:
        courses = courses.filter(
            duration__icontains=duration
        )

    # Minimum Fees
    if min_fees:
        courses = courses.filter(
            fees__gte=min_fees
        )

    # Maximum Fees
    if max_fees:
        courses = courses.filter(
            fees__lte=max_fees
        )

    # Ordering
    if order == 'low':
        courses = courses.order_by('fees')

    elif order == 'high':
        courses = courses.order_by('-fees')

    return render(request,'course_list.html',
        {
            'courses': courses
        }
    )
def course_create(request):

    if request.method == "POST":

        form = CourseForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm()

    return render(request, "course_form.html", {
        "form": form
    })

def course_detail(request, id):
    course = Course.objects.get(id=id)

    return render(request, "course_details.html", {
        "course": course
    })


def course_update(request, id):
    course = Course.objects.get(id=id)

    if request.method == "POST":
        form = CourseForm(request.POST,request.FILES,instance=course
        )

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm(instance=course)

    return render(request, "course_form.html", {
        "form": form
    })


def course_delete(request, id):
    course = Course.objects.get(id=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "course_delete.html", {
        "course": course
    })



#entrollment

def enrollment_list(request):

    enrollments = Enrollment.objects.all()

    course = request.GET.get("course")
    student = request.GET.get("student")
    status = request.GET.get("status")

    if course:
        enrollments = enrollments.filter(course_id=course)

    if student:
        enrollments = enrollments.filter(student_id=student)

    if status:
        enrollments = enrollments.filter(status=status)

    courses = Course.objects.all()
    students = Student.objects.all()

    return render(request, "enr_list.html", {
        "enrollments": enrollments,
        "courses": courses,
        "students": students,
    })


def enrollment_create(request):

    if request.method == "POST":

        form = EnrollForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("enrollment_list")

    else:
        form = EnrollForm()

    return render(request, "enr_form.html", {
        "form": form
    })


def enrollment_detail(request, id):

    enrollment = Enrollment.objects.get(id=id)

    return render(request, "enr_details.html", {
        "enrollment": enrollment
    })


def enrollment_update(request, id):

    enrollment = Enrollment.objects.get(id=id)

    if request.method == "POST":

        form = EnrollForm(
            request.POST,
            instance=enrollment
        )

        if form.is_valid():
            form.save()

            return redirect("enrollment_list")

    else:
        form = EnrollForm(
            instance=enrollment
        )

    return render(request, "enr_form.html", {
        "form": form
    })


def enrollment_delete(request, id):

    enrollment = Enrollment.objects.get(id=id)

    if request.method == "POST":

        enrollment.delete()

        return redirect("enrollment_list")

    return render(request, "enr_delete.html", {
        "enrollment": enrollment
    })


# instructor

def instructor_list(request):

    instructors = Instructor.objects.all()

    return render(request, "ins_list.html", {
        "instructors": instructors
    })


def instructor_create(request):

    if request.method == "POST":

        form = InstructorForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("instructor_list")

    else:
        form = InstructorForm()

    return render(request, "ins_form.html", {
        "form": form
    })

def instructor_detail(request, id):

    instructor = Instructor.objects.get(id=id)

    return render(request, "ins_detail.html", {
        "instructor": instructor
    })


def instructor_update(request, id):

    instructor = Instructor.objects.get(id=id)

    if request.method == "POST":

        form = InstructorForm(
            request.POST,
            request.FILES,
            instance=instructor
        )

        if form.is_valid():
            form.save()
            return redirect("instructor_list")

    else:
        form = InstructorForm(
            instance=instructor
        )

    return render(request, "ins_form.html", {
        "form": form,
        "instructor": instructor
    })


def instructor_delete(request, id):

    instructor = Instructor.objects.get(id=id)

    if request.method == "POST":

        instructor.delete()

        return redirect("instructor_list")

    return render(request, "ins_delete.html", {
        "instructor": instructor
    })

#material

def material_list(request):
    materials = CourseMaterial.objects.all()

    return render(request, "mat_list.html", {
        "materials": materials
    })

def material_create(request):

    if request.method == "POST":

        form = MaterialForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("material_list")

    else:
        form = MaterialForm()

    return render(request, "mat_form.html", {
        "form": form
    })

def material_detail(request, id):

    material = CourseMaterial.objects.get(id=id)

    return render(request, "mat_details.html", {
        "material": material
    })

def material_update(request, id):

    material = CourseMaterial.objects.get(id=id)

    if request.method == "POST":

        form = MaterialForm(
            request.POST,
            request.FILES,
            instance=material
        )

        if form.is_valid():
            form.save()
            return redirect("material_list")

    else:

        form = MaterialForm(
            instance=material
        )

    return render(request, "mat_form.html", {
        "form": form,
        "material": material
    })

def material_delete(request, id):

    material = CourseMaterial.objects.get(id=id)

    if request.method == "POST":
        material.delete()
        return redirect("material_list")

    return render(request, "mat_delete.html", {
        "material": material
    })

#dashboard
from django.db.models import Count, Avg, Max, Min
def dashboard(request):

    

    # Total statistics
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()

    # Marks statistics
    marks_data = Enrollment.objects.aggregate(
        average=Avg("marks"),
        highest=Max("marks"),
        lowest=Min("marks")
    )

    average_marks = marks_data["average"] or 0
    highest_marks = marks_data["highest"] or 0
    lowest_marks = marks_data["lowest"] or 0

    # Course-wise student count
    course_data = Course.objects.annotate(
        student_count=Count("enrollment")
    )

    # Student-wise course count
    student_data = Student.objects.annotate(
        course_count=Count("enrollment")
    )

    return render(request, "dashboard.html", {

        "total_students": total_students,
        "total_courses": total_courses,
        "total_enrollments": total_enrollments,

        "average_marks": round(average_marks, 1),
        "highest_marks": highest_marks,
        "lowest_marks": lowest_marks,

        "course_data": course_data,
        "student_data": student_data,
    })


from django.contrib import messages
def signup(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(request, "Account created successfully.")
        return redirect("login")

    return render(request, "signup.html")


from django.contrib.auth import authenticate, login, logout
def login_view(request):
    

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, "login.html")

def home(request):
    
    return render(request,"home.html")

def logout_view(request):
    logout(request)
    return redirect("home")