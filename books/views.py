from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book
# Create your views here.

class HomePageView(TemplateView):
	template_name = 'home.html'

class ListPageView(ListView):
	model = Book
	template_name= 'list.html'

class DetailPageView(DetailView):
	model= Book
	template_name = 'detail.html'

class AddressPageView(TemplateView):
	template_name = 'address.html'