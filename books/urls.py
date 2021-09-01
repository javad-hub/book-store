from django.urls import path
from .views import HomePageView, ListPageView, DetailPageView

urlpatterns = [
	path('', HomePageView.as_view(), name="home"),
	path('list/', ListPageView.as_view(), name="list"),
	path('<int:pk>', DetailPageView.as_view(), name="detail"),
]