from django.urls import path
from . import views

app_name = "stake"

urlpatterns = [
	path("pools/", views.IndexView, name="pool"),
	path("stake/", views.StakeView, name="stake"),
	path("harvest/", views.HarvestView, name="harvest"),
]