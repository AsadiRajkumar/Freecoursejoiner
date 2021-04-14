from django.contrib import admin
from django.urls import path, include
from myfirst import views

urlpatterns = [
	path("",views.home,name="home"),
	path("contact",views.contact,name="contact"),
	path("about",views.about,name="about"),
	path("Categories/courses",views.courses,name="Categories/courses"),
	path("Categories/Jobs",views.Jobs,name="Categories/Jobs"),
	path("Categories/Udemy",views.Udemy,name="Categories/Udemy"),
]
