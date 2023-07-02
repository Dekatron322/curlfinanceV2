from django.urls import path
from . import views

app_name = "launchpad"

urlpatterns = [
	path("", views.IndexView, name="launchpad"),
    
	path("add-ido/", views.AddIdoView, name="add_ido"),
    path("fund-presale/<int:ido_id>/", views.FundPresaleView, name="fund_presale"),
	path("details/<int:ido_id>/", views.DetailsView, name="details"),
	path("contribute/<int:ido_id>/", views.ContributeView, name="contribute"),
    
    path("my-presales/", views.MyPresalesView, name="my_presales"),
    path("my-idos/", views.MyIdosView, name="my_idos"),
    path("my-contributions/", views.MyContributionsView, name="my_contributions"),
    
    path("claim/<int:ido_id>/", views.ClaimView, name="claim"),
    path("emergency-withdraw/<int:ido_id>/", views.EWithdrawView, name="e_withdraw"),
    path("end-presale/", views.EndPresaleView, name="end_presale"),

    path("withdraw-project-token/<int:ido_id>/", views.WithdrawPtView, name="withdraw_project_token"),
    path("withdraw-contributed-token/<int:ido_id>/", views.WithdrawCtView, name="withdraw_contributed_token"),


]

