from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Course
from .forms import *


# Create your views here.
def list_courses(request):
    print(request)
    courses = Course.objects.all()
    data = {"courses": list(courses.values("id", "name", "description"))}
    return JsonResponse(data)


def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    data = {
        "name": course.name,
        "description": course.description,
    }
    return JsonResponse(data)


# def course_detail(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     data = {
#         "name": course.name,
#         "description": course.description,
#     }
#     return JsonResponse(data)


def create_course(request):
    if request.method == "POST":
        form = CreateNewCourse(request.POST)
        if form.is_valid():
            name = form["name"].value()
            description = form["description"].value()
            Course.objects.create(name=name, description=description)
            return HttpResponse("Course created")
    else:
        return render(
            request,
            "create_course.html",
            {"form": CreateNewCourse(), "form2": CreateNewCourseTest()},
        )


def new_course(request, course_name):
    Course.objects.create(name=course_name, description="A new course")
    courses = Course.objects.all()
    data = {"courses": list(courses.values("id", "name", "description"))}
    return JsonResponse(data)


def create_dummies(request):
    Course.objects.all().delete()
    # reset id sequence to 1
    Course.objects.raw("ALTER SEQUENCE courses_course_id_seq RESTART WITH 1;")

    Course.objects.create(
        name="Python Basics", description="Learn the basics of Python"
    )
    Course.objects.create(
        name="Python Intermediate", description="Learn intermediate Python"
    )
    Course.objects.create(name="Python Advanced", description="Learn advanced Python")
    return HttpResponse("Dummy courses created")
