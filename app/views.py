from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Book
from templates.forms import ReviewForm


def home(request):
  template = loader.get_template('app.html')
  context = {
    'books': Book.objects.all(),
  }
  return HttpResponse(template.render(context, request))

def book(req, slug):
  return HttpResponse("<h1>Wow!</h1>")

def review(request):
  if request.method == "POST":
    form = ReviewForm(request.POST or None)

    if form.is_valid():
      form.save()

      return HttpResponseRedirect("http://www.google.com")
  else:
    form = ReviewForm()

  return render(request, 'reviews.html', {"form": form })



