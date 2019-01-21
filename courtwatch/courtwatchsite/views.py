from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from .forms import StoryForm
from .models import Story


# Create your views here.



context = { }

def index(request):
	return render(request, 'index.html', context)

def stories(request):
    obj = Story.objects.last()

    context = {
        'title': obj.title,
        'text': obj.text,
        'id': obj.id,
        'last': last
    }

    return render(request, "stories.html", context)

def next(request, pk):
    pk = int(pk)
    n = pk - 1
    obj = Story.objects.get(id=n)

    context = {'title': obj.title, 'text': obj.text, 'id': n}

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
	form = StoryForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, 'member.html', context)

