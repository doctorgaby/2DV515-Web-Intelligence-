from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	#return HttpResponse("<h1>Assignment 1 - Movie Recommendation System</h1>") #string of HTML code useful if you want only one
	#the custom django function takes a request, a template name(from templates folder) and a context(empty dictionary)
	return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})
