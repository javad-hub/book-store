from django.urls import path
from .views import HomePageView, ListPageView, DetailPageView, AddressPageView

urlpatterns = [
	path('', HomePageView.as_view(), name="home"),
	path('list/', ListPageView.as_view(), name="list"),
	path('<int:pk>', DetailPageView.as_view(), name="detail"),
	path('address/', AddressPageView.as_view(), name="address"),
]