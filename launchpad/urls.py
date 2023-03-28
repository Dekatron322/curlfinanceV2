from django.urls import path
from . import views

app_name = "launchpad"

urlpatterns = [
	path("launchpad/", views.IndexView, name="launchpad"),
	path("details/", views.DetailsView, name="details"),
	path("contribute/", views.ContributeView, name="contribute"),
]