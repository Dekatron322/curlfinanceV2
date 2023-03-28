from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

    path("your-portfolio/manual/", views.ConnectMetamaskManualView, name="your_portfolio_manual"),
    path("your-portfolio/bitgert/", views.ConnectMetamaskManualBView, name="your_portfolio_bitgert"),
    path("your-portfolio/bsc/", views.ConnectMetamaskManualBscView, name="your_portfolio_bsc"),
    path("your-portfolio/canto/", views.ConnectMetamaskManualCantoView, name="your_portfolio_canto"),
    path("your-portfolio/core/", views.ConnectMetamaskManualCoreView, name="your_portfolio_core"),
    path("your-portfolio/", views.ConnectMetamaskView, name="your_portfolio"),
    path("bitgert-portfolio/", views.BitgertConnectMetamaskView, name="bitgert_portfolio"),
    path("bsc-portfolio/", views.BscConnectMetamaskView, name="bsc_portfolio"),
    path("canto-portfolio/", views.CantoConnectMetamaskView, name="canto_portfolio"),
    path("core-portfolio/", views.CoreConnectMetamaskView, name="core_portfolio"),
    path("portfolio/", views.PortfolioView, name="portfolio"),
    path("bscportfolio/", views.BscPortfolioView, name="bscportfolio"),
    path("brise-portfolio/", views.BrisePortfolioView, name="brise_portfolio"),
    path("wcanto-portfolio/", views.WCantoPortfolioView, name="wcanto_portfolio"),
    path("coreportfolio/", views.CorePortfolioView, name="coreportfolio"),
	path("", views.IndexView, name="index"),
	path("doken/", views.DokenView, name="doken"),
	path("loop/", views.LoopView, name="loop"),
	path("candy/", views.CandyView, name="candy"),
	path("ice/", views.IceView, name="ice"),
	path("navis/", views.NavisView, name="navis"),
	path("bow/", views.BowView, name="bow"),
	path("lung/", views.LungView, name="lung"),
	path("bitgert/", views.BitgertView, name="bitgert"),
	path("canto/", views.CantoView, name="canto"),
	path("core/", views.CoreView, name="core"),
	path("coming/", views.ComingView, name="coming"),
	path("shadowswap/", views.ShadowView, name="shadowswap"),
	path("coreid/", views.CoreidView, name="coreid"),
	path("crest/", views.CrestView, name="crest"),
	path("yieldz/", views.YieldsView, name="yieldz"),
	path("happy/", views.HappyView, name="happy"),
	path("lfgswap/", views.LfgswapView, name="lfgswap"),
	path("4token/", views.IgnoreFudView, name="4token"),

]