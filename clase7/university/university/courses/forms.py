from django import forms


class CreateNewCourse(forms.Form):
    name = forms.CharField(max_length=100, label="Course Name")
    description = forms.CharField(widget=forms.Textarea, label="Course Description")


class CreateNewCourseTest(forms.Form):
    name = forms.CharField(max_length=100, label="Course Name")
    description = forms.CharField(widget=forms.Textarea, label="Course Description")
    edad = forms.IntegerField(label="Edad")
    email = forms.EmailField(label="Email")
