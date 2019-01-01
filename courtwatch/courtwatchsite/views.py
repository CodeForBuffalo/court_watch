from django.shortcuts import render, render_to_response

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
	return render_to_response('join.html')
def contact(request):
	return render_to_response('contact.html')
def login(request):
	return render_to_response('login.html')
def member(request):
	return render_to_response('member.html')

