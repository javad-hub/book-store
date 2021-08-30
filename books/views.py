from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book
# Create your views here.

class HomePageView(TemplateView):
	model = Book
	template_name = 'home.html'