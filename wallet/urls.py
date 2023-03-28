from django.urls import path
from . import views

app_name = "wallet"

urlpatterns = [

	path("", views.CoreView, name="wallet"),
	path("bitrise-wallet/", views.BitriseView, name="bitrise_wallet"),
	path("bsc-wallet/", views.BscView, name="bsc_wallet"),
	path("lung-wallet/", views.LungView, name="lung_wallet"),
	path("canto-wallet/", views.CantoView, name="canto_wallet"),
	path("doken-wallet/", views.DokenView, name="doken_wallet"),
	path("withdraw/", views.SendView, name="withdraw"),
	path("profile/", views.ProfileView, name="profile"),
	path("send-token/<str:token_address>/", views.SendTokenView, name="send_token"),
	path("send-bitrise-token/<str:token_address>/", views.SendBitriseTokenView, name="send_bitrise_token"),
	path("send-bsc-token/<str:token_address>/", views.SendBscTokenView, name="send_bsc_token"),
	path("lung-bsc-token/<str:token_address>/", views.SendLungTokenView, name="send_lung_token"),
	path("send-canto-token/<str:token_address>/", views.SendCantoTokenView, name="send_canto_token"),
	path("send-core-token/<str:token_address>/", views.SendCoreTokenView, name="send_core_token"),
	
	
	
]