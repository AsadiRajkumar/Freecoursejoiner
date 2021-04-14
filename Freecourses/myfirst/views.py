from django.shortcuts import render
from django.http import HttpResponse
from .models import Internship,Freecourses,Udemycourse
from Freecourses.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
	udemy=Udemycourse.objects.all().order_by("-Date")[:4]
	jobs=Internship.objects.all().order_by("-Date")[:2]
	return render(request,'home.html',{'udemy':udemy,'jobs':jobs})

def contact(request):
	if request.method=="POST":
		name="name :"+request.POST.get('name')+"\n"
		name+="Email :"+request.POST.get('Email')+"\n"
		subject=request.POST.get('Subject')
		name+="Description :"+request.POST.get('description')
		if send_mail(subject,name,EMAIL_HOST_USER,[EMAIL_HOST_USER],fail_silently=False):
			print("successfully sended")
	return render(request,'contact.html')
	
	
def about(request):
	return render(request,'about.html',{'title':'about'})
	
def courses(request):
	freecourses=Freecourses.objects.all().order_by("-Date")
	return render(request,'Categories/courses.html',{'freecourses':freecourses})

	
	
	
	
	
	
def Jobs(request):
	jobs=Internship.objects.all().order_by("-Date")
	page = request.GET.get('page')
	paginator = Paginator(jobs,20)
	try:
		jobs = paginator.page(page)
	except PageNotAnInteger:
		jobs = paginator.page(1)
	except EmptyPage:
		jobs = paginator.page(paginator.num_pages)
	return render(request,'Categories/Jobs.html',{'jobs':jobs})
	
	
	

	
def Udemy(request):
	udemy=Udemycourse.objects.all().order_by("-Date")
	return render(request,'Categories/Udemy.html',{'udemy':udemy})

