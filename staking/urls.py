from django.urls import path
from . import views

app_name = "stake"

urlpatterns = [
	path("pools/<int:ido_id>/", views.IndexView, name="pool"),
	path("stake/<int:ido_id>/<int:amount>/", views.StakeView, name="stake"),
    path("my-stakes/", views.MyStakesView, name="my_stakes"),
	path("harvest/<int:stake_id>/", views.HarvestView, name="harvest"),
]