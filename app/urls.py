from django.contrib import admin
from django.urls import path

from . import views
from .views import home, book, review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('review', review, name='review'),
    path('<slug:slug>', book, name="<slug>"),
]
