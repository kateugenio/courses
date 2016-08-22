from django.shortcuts import render, redirect, HttpResponse
from . import models

# Create your views here.
def index(request):
	allCourses = models.Course.objects.all()
	context = {'allcourses':allCourses}
	return render(request, 'coursesapp/index.html', context)

def create(request):
	name = request.POST['coursename']
	description = request.POST['description']
	course = models.Course.objects.create(name=name, description=description)
	return redirect('/')

def showOne(request, id):
	course = models.Course.objects.get(pk=id)
	print course
	context = {'course':course}
	return render(request, 'coursesapp/destroyoneshow.html', context)

def destroy(request, id):
	destroy_course = models.Course.objects.get(pk=id).delete()
	return redirect('/')