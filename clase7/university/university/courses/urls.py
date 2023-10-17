from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.list_courses),
    path("all/<int:course_id>/", views.course_detail),
    path("new_course/<str:course_name>/", views.new_course),
    path("create_course/", views.create_course),
    path("create_dummies/", views.create_dummies),
]
