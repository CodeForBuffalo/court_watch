from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required


# Create your views here.



context = { }

def index(request):
	return render(request, 'index.html', context)

def stories(request):
    return render(request, "stories.html", context)


def statistics(request):
    return render(request, 'statistics.html', context)


def resources(request):
    return render(request, 'resources.html', context)

def join(request):
	return render(request, 'join.html', context)
def contact(request):
	return render(request, 'contact.html', context)
def login(request):
	return render(request, 'login.html', context)

@login_required
def member(request):
	return render(request, 'member.html', context)

