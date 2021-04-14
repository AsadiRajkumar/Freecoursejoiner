from django.contrib import admin

# Register your models here.

from .models import Internship,Freecourses,Udemycourse
	
	
admin.site.register(Internship)
admin.site.register(Freecourses)
admin.site.register(Udemycourse)

