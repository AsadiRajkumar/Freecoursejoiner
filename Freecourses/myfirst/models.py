from django.db import models

# Create your models here.


class Internship(models.Model):
	title=models.TextField(max_length=100)
	titledescription=models.TextField(max_length=200)
	about=models.TextField(max_length=100)
	aboutjob=models.TextField(max_length=500)
	hiringdetails=models.TextField(max_length=500)
	Eligibility=models.TextField(max_length=1000)
	applylink=models.TextField(max_length=100)
	Date=models.DateTimeField(auto_now_add=False,auto_now=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	
class Freecourses(models.Model):
	title=models.TextField(max_length=100)
	coursename=models.TextField(max_length=500)
	link=models.TextField(max_length=200)
	Date=models.DateTimeField(auto_now_add=False,auto_now=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)

class Udemycourse(models.Model):
	pic=models.ImageField(upload_to="pics")
	coursetitle=models.TextField(max_length=500)
	link=models.TextField(max_length=200)
	Date=models.DateTimeField(auto_now_add=False,auto_now=True)
