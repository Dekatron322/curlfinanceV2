from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required




from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

#from .forms import UserForm

from datetime import datetime
from requests import Request, Session
import json
import time
from datetime import datetime, timedelta





def ConnectMetamaskManualView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:portfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_manual.html", context)
		
def ConnectMetamaskManualBView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:brise_portfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_bitgert_manual.html", context)
		
def ConnectMetamaskManualBscView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:bscportfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_bsc_manual.html", context)
		
def ConnectMetamaskManualCoreView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:coreportfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_core_manual.html", context)
		
		
def ConnectMetamaskManualCantoView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:wcanto_portfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_canto_manual.html", context)
		
def ConnectMetamaskView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:portfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask.html", context)
		
def BitgertConnectMetamaskView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:brise_portfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_bitgert.html", context)
		
def BscConnectMetamaskView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:bscportfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_bsc.html", context)
		
def CoreConnectMetamaskView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:coreportfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_core.html", context)
		
def CantoConnectMetamaskView(request):
	if request.method == "POST":
		wallet = request.POST.get("wallet")
		request.session["wallet"] = wallet
		
		return HttpResponseRedirect(reverse("main:wcanto_portfolio"))
		

	else:

		context = {}
		return render(request, "main/connect_metamask_canto.html", context)

def BrisePortfolioView(request):
	if request.method == "POST":
		pass

	else:
		try:
			total = 0
			wallet = request.session["wallet"]
			
			resp = requests.get("https://api.iotexchartapp.com/bitrise-get-balance/%s/" % str(wallet)).json()
			data = resp["data"]
			
			for item in data:
				total += float(item['total_price'])

			#return HttpResponse(data)
			context = {"data": data, "total": total, "wallet": wallet}
			return render(request, "main/brise_portfolio.html", context)
			
		except:
			return HttpResponseRedirect(reverse("main:bitgert_portfolio"))
			
def BscPortfolioView(request):
	if request.method == "POST":
		pass

	else:
		try:
			total = 0
			wallet = request.session["wallet"]
			
			resp = requests.get("https://api.iotexchartapp.com/bsc-get-balance/%s/" % str(wallet)).json()
			data = resp["data"]
			
			for item in data:
				total += float(item['total_price'])

			#return HttpResponse(data)
			context = {"data": data, "total": total, "wallet": wallet}
			return render(request, "main/bscportfolio.html", context)
			
		except:
			return HttpResponseRedirect(reverse("main:bsc_portfolio"))
			
def CorePortfolioView(request):
	if request.method == "POST":
		pass

	else:
		try:
			total = 0
			wallet = request.session["wallet"]
			
			resp = requests.get("https://api.iotexchartapp.com/coredao-get-balance/%s/" % str(wallet)).json()
			data = resp["data"]
			
			for item in data:
				total += float(item['total_price'])

			#return HttpResponse(data)
			context = {"data": data, "total": total, "wallet": wallet}
			return render(request, "main/coreportfolio.html", context)
			
		except:
			return HttpResponseRedirect(reverse("main:core_portfolio"))
			
def WCantoPortfolioView(request):
	if request.method == "POST":
		pass

	else:
		try:
			total = 0
			wallet = request.session["wallet"]
			
			resp = requests.get("https://api.iotexchartapp.com/canto-get-balance/%s/" % str(wallet)).json()
			data = resp["data"]
			
			for item in data:
				total += float(item['total_price'])

			#return HttpResponse(data)
			context = {"data": data, "total": total, "wallet": wallet}
			return render(request, "main/canto_portfolio.html", context)
			
		except:
			return HttpResponseRedirect(reverse("main:canto_portfolio"))


def PortfolioView(request):
	if request.method == "POST":
		pass

	else:
		try:
			total = 0
			wallet = request.session["wallet"]
			
			resp = requests.get("https://api.iotexchartapp.com/loop-get-balance/%s/" % str(wallet)).json()
			data = resp["data"]
			
			for item in data:
				total += float(item['total_price'])

			#return HttpResponse(data)
			context = {"data": data, "total": total, "wallet": wallet}
			return render(request, "main/portfolio.html", context)
			
		except:
			return HttpResponseRedirect(reverse("main:your_portfolio"))



def NoneView(request):
	if request.method == "POST":
		pass

	else:

		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crypto-com-chain&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		doken = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=doken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		
		context = {"cronos":cronos, "doken":doken, "data":data,}
		return render(request, "main/none.html", context)

def GetUrlViaAddress(address):
		
	if address == "0x27b45bCC26e01Ed50B4080A405D1c492FEe89d63":
		url = "doken"
	elif address == "0xce186ad6430e2fe494a22c9edbd4c68794a28b35":
		url = "loop"
	#elif address == "0xeA8686a739550d9C88FaEfb39aC6cb78B6288767":
	    #url = "candy"
	elif address == "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d":
	    url = "ice"
	#
	elif address == "0x8fff93e810a2edaafc326edee51071da9d398e83":
	    url = "bitgert"
	elif address == "0x826551890dc65655a0aceca109ab11abdbd7a07b":
	    url = "canto"
	
	elif address == "0x43a8a925c1930A313D283359184A64c51a2bc0E9":
	    url = "navis"
	elif address == "0x28b9aed756de31b6b362aa0f23211d13093ebb79":
	    url = "lung"
	elif address == "0x81bCEa03678D1CEF4830942227720D542Aa15817":
	    url = "core"
	elif address == "0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5":
	    url = "shadowswap"
	elif address == "0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4":
	    url = "bow"
	elif address == "0xb999ea90607a826a3e6e6646b404c3c7d11fa39d":
	    url = "ice"
	elif address == "0x000000000e1d682cc39abe9b32285fdea1255374":
	    url = "coreid"
	elif address == "0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84":
	    url = "crest"
	elif address == "0xe191a4d47A6be111C75139757CDDBb61BEEd88FB":
	    url = "yieldz"
	elif address == "0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D":
	    url = "lfgswap"
	elif address == "0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4":
	    url = "happy"

	else:
		url = "loop"


	return url

def GetUrlViaName(name):

	if name == "Doken Super Chain (DSC)":
		url = "doken"
	elif name == "LoopNetwork (LOOP)":
		url = "loop"
	#elif name == "CandySwap (CANDY)":
	    #url = "candy"
	elif name == "IceCreamSwap (ICE)":
	    url = "ice"
	elif name == "Bitgert (Brise)":
	    url = "bitgert"
	elif name == "Canto (CANTO)":
	    url = "canto"
	elif name == "Navis (NVS)":
	    url = "navis"
	elif name == "Lunagens (LUNG)":
	    url = "lung"
	elif name == "Coredao (CORE)":
	    url = "core"
	elif name == "ShadowSwap (SHADOW)":
	    url = 'shadowswap'
	elif name == "Archerswap (BOW)":
	    url = "bow"
	elif name == "Icecreamswap (ICE)":
	    url = "ice"
	elif name == "Coreid (COREID)":
	    url = "coreid"
	elif name == "Crest Protocol (CPT)":
	    url = "crest"
	elif name == "Yieldz (YZ)":
	    url = "yieldz"
	elif name == "LFGSwap (LFG)":
	    url = "lfgswap"
	elif name == "Happy Token (HAPPY)":
	    url = "happy"
    
	    
	else:
		url = "loop"

	return url


def IndexView(request):
	if request.method == "POST":
		address_db = [
		"0x27b45bCC26e01Ed50B4080A405D1c492FEe89d63",
		"0xce186ad6430e2fe494a22c9edbd4c68794a28b35",
		"0xb999ea90607a826a3e6e6646b404c3c7d11fa39d",
		"0x8fff93e810a2edaafc326edee51071da9d398e83",
		"0x826551890dc65655a0aceca109ab11abdbd7a07b",
		"0x43a8a925c1930A313D283359184A64c51a2bc0E9",
		"0x28b9aed756de31b6b362aa0f23211d13093ebb79",
		"0x81bCEa03678D1CEF4830942227720D542Aa15817",
		"0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5",
		"0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4",
		"0xb999ea90607a826a3e6e6646b404c3c7d11fa39d",
		"0x000000000e1d682cc39abe9b32285fdea1255374",
		"0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84",
		"0xe191a4d47A6be111C75139757CDDBb61BEEd88FB",
		"0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D",
		"0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4",
		]

		name_db = ["Doken Super Chain (DSC)", "LoopNetwork (LOOP)", "IceCreamSwap (ICE)", "Bitgert (BRISE)", "Canto (Canto)", "Navis (NVS)", "Lunagens (LUNG)", "ShadowSwap (SHADOW)", "Coredao (CORE)", "Archerswap (BOW)", "Icecreamswap (ICE)", "Coreid (coreid)", "Crest Protocol (CPT)", "Yieldz (YZ)", "LFGSwap (LFG)", "Happy Token (HAPPY)"]

		status = False
		result = None
		url = "none"

		query = request.POST.get("query")

		if query[0]+query[1] == "0x":
			for item in address_db:
				if query == item:
					result = item
					url = GetUrlViaAddress(result)


		for item in name_db:
			if query == item or query in item:
				result = item

				url = GetUrlViaName(result)


		return HttpResponseRedirect(reverse("main:%s" % (url)))
		


	else:
		#data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		#doken = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=doken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		
		
		#candy = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xeA8686a739550d9C88FaEfb39aC6cb78B6288767")
		
		#candydekatron = candy.json()
		#candypairs = candydekatron["pairs"][0]
		#candybaseToken = candypairs["baseToken"]
		#candypriceNative = candypairs["priceNative"]
		#candypriceUsd = candypairs["priceUsd"]
		#candyvolume = candypairs["volume"]
		#candypriceChange = candypairs["priceChange"]
		#candyfdv = candypairs["fdv"]
		
		coredao = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x81bCEa03678D1CEF4830942227720D542Aa15817")
		
		coredaodekatron = coredao.json()
		coredaopairs = coredaodekatron["pairs"][0]
		coredaobaseToken = coredaopairs["baseToken"]
		coredaopriceNative = coredaopairs["priceNative"]
		coredaopriceUsd = coredaopairs["priceUsd"]
		coredaovolume = coredaopairs["volume"]
		coredaopriceChange = coredaopairs["priceChange"]
		coredaofdv = coredaopairs["fdv"]
		
		ice = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xb999ea90607a826a3e6e6646b404c3c7d11fa39d")
		icedekatron = ice.json()
		icepairs = icedekatron["pairs"][0]
		icebaseToken = icepairs["baseToken"]
		icepriceNative = icepairs["priceNative"]
		icepriceUsd = icepairs["priceUsd"]
		icevolume = icepairs["volume"]
		icepriceChange = icepairs["priceChange"]
		icefdv = icepairs["fdv"]
		
		bitrise = requests.get("https://api.dexscreener.com/latest/dex/tokens/	0x8fff93e810a2edaafc326edee51071da9d398e83")
		bitrisedekatron = bitrise.json()
		bitrisepairs = bitrisedekatron["pairs"][0]
		bitrisebaseToken = bitrisepairs["baseToken"]
		bitrisepriceNative = bitrisepairs["priceNative"]
		bitrisepriceUsd = bitrisepairs["priceUsd"]
		bitrisevolume = bitrisepairs["volume"]
		bitrisepriceChange = bitrisepairs["priceChange"]
		bitrisefdv = bitrisepairs["fdv"]
		
		canto = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x826551890dc65655a0aceca109ab11abdbd7a07b")
		cantodekatron = canto.json()
		cantopairs = cantodekatron["pairs"][0]
		cantobaseToken = cantopairs["baseToken"]
		cantopriceNative = cantopairs["priceNative"]
		cantopriceUsd = cantopairs["priceUsd"]
		cantovolume = cantopairs["volume"]
		cantopriceChange = cantopairs["priceChange"]
		cantofdv = cantopairs["fdv"]
		
		fuse = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x0be9e53fd7edac9f859882afdda116645287c629")
		fusedekatron = fuse.json()
		fusepairs = fusedekatron["pairs"][1]
		fusebaseToken = fusepairs["baseToken"]
		fusepriceNative = fusepairs["priceNative"]
		fusepriceUsd = fusepairs["priceUsd"]
		fusevolume = fusepairs["volume"]
		fusepriceChange = fusepairs["priceChange"]
		fusefdv = fusepairs["fdv"]
		
		hash = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xb3999f658c0391d94a37f7ff328f3fec942bcadc")
		hashdekatron = hash.json()
		hashpairs = hashdekatron["pairs"][0]
		hashbaseToken = hashpairs["baseToken"]
		hashpriceNative = hashpairs["priceNative"]
		hashpriceUsd = hashpairs["priceUsd"]
		hashvolume = hashpairs["volume"]
		hashpriceChange = hashpairs["priceChange"]
		hashfdv = hashpairs["fdv"]
		
		canto = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x826551890dc65655a0aceca109ab11abdbd7a07b")
		cantodekatron = canto.json()
		cantopairs = cantodekatron["pairs"][0]
		cantobaseToken = cantopairs["baseToken"]
		cantopriceNative = cantopairs["priceNative"]
		cantopriceUsd = cantopairs["priceUsd"]
		cantovolume = cantopairs["volume"]
		cantopriceChange = cantopairs["priceChange"]
		cantofdv = cantopairs["fdv"]
		
		navis = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x43a8a925c1930A313D283359184A64c51a2bc0E9")
		navisdekatron = navis.json()
		navispairs = navisdekatron["pairs"][0]
		navisbaseToken = navispairs["baseToken"]
		navispriceNative = navispairs["priceNative"]
		navispriceUsd = navispairs["priceUsd"]
		navisvolume = navispairs["volume"]
		navispriceChange = navispairs["priceChange"]
		navisfdv = navispairs["fdv"]
		
		bow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4")
		bowdekatron = bow.json()
		bowpairs = bowdekatron["pairs"][0]
		bowbaseToken = bowpairs["baseToken"]
		bowpriceNative = bowpairs["priceNative"]
		bowpriceUsd = bowpairs["priceUsd"]
		bowvolume = bowpairs["volume"]
		bowpriceChange = bowpairs["priceChange"]
		bowfdv = bowpairs["fdv"]
		
		shadow = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5")
		shadowdekatron = shadow.json()
		shadowpairs = shadowdekatron["pairs"][0]
		shadowbaseToken = shadowpairs["baseToken"]
		shadowpriceNative = shadowpairs["priceNative"]
		shadowpriceUsd = shadowpairs["priceUsd"]
		shadowvolume = shadowpairs["volume"]
		shadowpriceChange = shadowpairs["priceChange"]
		shadowfdv = shadowpairs["fdv"]
		
		coreid = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x000000000e1d682cc39abe9b32285fdea1255374")
		coreiddekatron = coreid.json()
		coreidpairs = coreiddekatron["pairs"][0]
		coreidbaseToken = coreidpairs["baseToken"]
		coreidpriceNative = coreidpairs["priceNative"]
		coreidpriceUsd = coreidpairs["priceUsd"]
		coreidvolume = coreidpairs["volume"]
		coreidpriceChange = coreidpairs["priceChange"]
		coreidfdv = coreidpairs["fdv"]
		
		crest = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84")
		crestdekatron = crest.json()
		crestpairs = crestdekatron["pairs"][0]
		crestbaseToken = crestpairs["baseToken"]
		crestpriceNative = crestpairs["priceNative"]
		crestpriceUsd = crestpairs["priceUsd"]
		crestvolume = crestpairs["volume"]
		crestpriceChange = crestpairs["priceChange"]
		crestfdv = crestpairs["fdv"]
		
		yields = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xe191a4d47A6be111C75139757CDDBb61BEEd88FB")
		yieldsdekatron = yields.json()
		yieldspairs = yieldsdekatron["pairs"][0]
		yieldsbaseToken = yieldspairs["baseToken"]
		yieldspriceNative = yieldspairs["priceNative"]
		yieldspriceUsd = yieldspairs["priceUsd"]
		yieldsvolume = yieldspairs["volume"]
		yieldspriceChange = yieldspairs["priceChange"]
		yieldsfdv = yieldspairs["fdv"]
		
		lfgswap = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D")
		lfgswapdekatron = lfgswap.json()
		lfgswappairs = lfgswapdekatron["pairs"][0]
		lfgswapbaseToken = lfgswappairs["baseToken"]
		lfgswappriceNative = lfgswappairs["priceNative"]
		lfgswappriceUsd = lfgswappairs["priceUsd"]
		lfgswapvolume = lfgswappairs["volume"]
		lfgswappriceChange = lfgswappairs["priceChange"]
		lfgswapfdv = lfgswappairs["fdv"]
		
		happy = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4")
		happydekatron = happy.json()
		happypairs = happydekatron["pairs"][0]
		happybaseToken = happypairs["baseToken"]
		happypriceNative = happypairs["priceNative"]
		happypriceUsd = happypairs["priceUsd"]
		happyvolume = happypairs["volume"]
		happypriceChange = happypairs["priceChange"]
		happyfdv = happypairs["fdv"]
		
		lung = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x28b9aed756de31b6b362aa0f23211d13093ebb79")
		lungdekatron = lung.json()
		lungpairs = lungdekatron["pairs"][0]
		lungbaseToken = lungpairs["baseToken"]
		lungpriceNative = lungpairs["priceNative"]
		lungpriceUsd = lungpairs["priceUsd"]
		lungvolume = lungpairs["volume"]
		lungpriceChange = lungpairs["priceChange"]
		lungfdv = lungpairs["fdv"]
		
		ignorefud = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E")
		ignorefuddekatron = ignorefud.json()
		ignorefudpairs = ignorefuddekatron["pairs"][0]
		ignorefudbaseToken = ignorefudpairs["baseToken"]
		ignorefudpriceNative = ignorefudpairs["priceNative"]
		ignorefudpriceUsd = ignorefudpairs["priceUsd"]
		ignorefudvolume = ignorefudpairs["volume"]
		ignorefudpriceChange = ignorefudpairs["priceChange"]
		ignorefudfdv = ignorefudpairs["fdv"]
		
		
		resp = requests.get("https://app.geckoterminal.com/api/p1/bitgert/pools/0x558077e98aeceeb1d616d18c144c15909d4ab744")
		getValue = resp.json()
		from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]

		context = {
		     
		    
		    
		    "coredaobaseToken":coredaobaseToken, 
		    "coredaovolume":coredaovolume, 
		    "coredaopriceChange":coredaopriceChange, 
		    "coredaopriceUsd":coredaopriceUsd, 
		    "coredaofdv":coredaofdv, 
		    
		    "ice":ice, 
		    "icebaseToken":icebaseToken, 
		    "icepriceNative":icepriceNative, 
		    "icepriceUsd":icepriceUsd, 
		    "icevolume":icevolume, 
		    "icepriceChange":icepriceChange, 
		    "icefdv":icefdv, 
		    
		    "bitrise":bitrise, 
		    "bitrisebaseToken":bitrisebaseToken, 
		    "bitrisepriceNative":bitrisepriceNative, 
		    "bitrisepriceUsd":bitrisepriceUsd, 
		    "bitrisevolume":bitrisevolume, 
		    "bitrisepriceChange":bitrisepriceChange, 
		    "bitrisefdv":bitrisefdv,
		    
		    "from_volume_in_usd":from_volume_in_usd, 
		    "canto":canto, 
		    "cantobaseToken":cantobaseToken, 
		    "cantopriceNative":cantopriceNative, 
		    "cantopriceUsd":cantopriceUsd, 
		    "cantovolume":cantovolume, 
		    "cantopriceChange":cantopriceChange, 
		    "cantofdv":cantofdv,
		    
		    "fuse":fuse, 
		    "fusebaseToken":fusebaseToken, 
		    "fusepriceNative":fusepriceNative, 
		    "fusepriceUsd":fusepriceUsd, 
		    "fusevolume":fusevolume, 
		    "fusepriceChange":fusepriceChange, 
		    "fusefdv":fusefdv, 
		    
		    "hash":hash, 
		    "hashbaseToken":hashbaseToken, 
		    "hashpriceNative":hashpriceNative, 
		    "hashpriceUsd":hashpriceUsd, 
		    "hashvolume":hashvolume, 
		    "hashpriceChange":hashpriceChange, 
		    "hashfdv":hashfdv,
		    
		    "navis":navis, 
		    "navisbaseToken":navisbaseToken, 
		    "navispriceNative":navispriceNative, 
		    "navispriceUsd":navispriceUsd, 
		    "navisvolume":navisvolume, 
		    "navispriceChange":navispriceChange, 
		    "navisfdv":navisfdv,
		    
		    "bow":bow, 
		    "bowbaseToken":bowbaseToken, 
		    "bowpriceNative":bowpriceNative, 
		    "bowpriceUsd":bowpriceUsd, 
		    "bowvolume":bowvolume, 
		    "bowpriceChange":bowpriceChange, 
		    "bowfdv":bowfdv,
		    
		    "shadow":shadow, 
		    "shadowbaseToken":shadowbaseToken, 
		    "shadowpriceNative":shadowpriceNative, 
		    "shadowpriceUsd":shadowpriceUsd, 
		    "shadowvolume":shadowvolume, 
		    "shadowpriceChange":shadowpriceChange, 
		    "shadowfdv":shadowfdv,
		    
		    "happy":happy, 
		    "happybaseToken":happybaseToken, 
		    "happypriceNative":happypriceNative, 
		    "happypriceUsd":happypriceUsd, 
		    "happyvolume":happyvolume, 
		    "happypriceChange":happypriceChange, 
		    "happyfdv":happyfdv,
		    
		    "coreid":coreid, 
		    "coreidbaseToken":coreidbaseToken, 
		    "coreidpriceNative":coreidpriceNative, 
		    "coreidpriceUsd":coreidpriceUsd, 
		    "coreidvolume":coreidvolume, 
		    "coreidpriceChange":coreidpriceChange, 
		    "coreidfdv":coreidfdv,
		    
		    "yields":yields, 
		    "yieldsbaseToken":yieldsbaseToken, 
		    "yieldspriceNative":yieldspriceNative, 
		    "yieldspriceUsd":yieldspriceUsd, 
		    "yieldsvolume":yieldsvolume, 
		    "yieldspriceChange":yieldspriceChange, 
		    "yieldsfdv":yieldsfdv,
		    
		    "crest":crest, 
		    "crestbaseToken":crestbaseToken, 
		    "crestpriceNative":crestpriceNative, 
		    "crestpriceUsd":crestpriceUsd, 
		    "crestvolume":crestvolume, 
		    "crestpriceChange":crestpriceChange, 
		    "crestfdv":crestfdv,
		    
		    "lfgswap":lfgswap, 
		    "lfgswapbaseToken":lfgswapbaseToken, 
		    "lfgswappriceNative":lfgswappriceNative, 
		    "lfgswappriceUsd":lfgswappriceUsd, 
		    "lfgswapvolume":lfgswapvolume, 
		    "lfgswappriceChange":lfgswappriceChange, 
		    "lfgswapfdv":lfgswapfdv,
		    
		    "lung":lung, 
		    "lungbaseToken":lungbaseToken, 
		    "lungpriceNative":lungpriceNative, 
		    "lungpriceUsd":lungpriceUsd, 
		    "lungvolume":lungvolume, 
		    "lungpriceChange":lungpriceChange, 
		    "lungfdv":lungfdv,
		    
		    "ignorefud":ignorefud, 
		    "ignorefudbaseToken":ignorefudbaseToken, 
		    "ignorefudpriceNative":ignorefudpriceNative, 
		    "ignorefudpriceUsd":ignorefudpriceUsd, 
		    "ignorefudvolume":ignorefudvolume, 
		    "ignorefudpriceChange":ignorefudpriceChange, 
		    "ignorefudfdv":ignorefudfdv,
		}
		return render(request, "main/index.html", context )

        
        
def DokenView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=doken&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=doken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0x0420eb45ac5a4f04763f679c07c3a637741e0289")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        volume = pairs["volume"]
        fdv = pairs["fdv"]
        price = str(response["doken"]["usd"])
        market_cap = int(response["doken"]["usd_market_cap"])
        hr_vol = str(response["doken"]["usd_24h_vol"])
        hr_chg = str(response["doken"]["usd_24h_change"])
        last_updated = str(response["doken"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd}
        return render(request, "main/doken.html", context)
        
def CoreView(request):
    if request.method == "POST":
        pass
    else:
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x81bCEa03678D1CEF4830942227720D542Aa15817")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bsc/pools/0xeb667758145bf8b9358f536284efa549f1d4d0cb")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/core.html", context)


def LoopView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=loopnetwork&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=loopnetwork&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0xce186ad6430e2fe494a22c9edbd4c68794a28b35")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        volume = pairs["volume"]
        fdv = pairs["fdv"]
        price = str(response["loopnetwork"]["usd"])
        market_cap = int(response["loopnetwork"]["usd_market_cap"])
        hr_vol = str(response["loopnetwork"]["usd_24h_vol"])
        hr_chg = str(response["loopnetwork"]["usd_24h_change"])
        last_updated = str(response["loopnetwork"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd}
        return render(request, "main/loop.html", context)
        
def CandyView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0xeA8686a739550d9C88FaEfb39aC6cb78B6288767")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns}
        return render(request, "main/candy.html", context)
        
def IceView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xb999ea90607a826a3e6e6646b404c3c7d11fa39d")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bitgert/pools/0x558077e98aeceeb1d616d18c144c15909d4ab744")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/ice.html", context)
        
def NavisView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x43a8a925c1930A313D283359184A64c51a2bc0E9")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bsc/pools/0xeb667758145bf8b9358f536284efa549f1d4d0cb")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/navis.html", context)
    
def BowView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/bow.html", context) 
        
def ShadowView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/shadow.html", context) 
        
def CoreidView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x000000000e1d682cc39abe9b32285fdea1255374")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/coreid.html", context)
        
def CrestView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xcFE4C0783d103C44f403Bb287d29af0bAE5D4E84")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/crest.html", context)
        
def YieldsView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xe191a4d47A6be111C75139757CDDBb61BEEd88FB")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/yieldz.html", context)
        
def HappyView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xAc9B3614Dd28c4ca72853CA996Ab76F03Db73Fb4")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/happy.html", context)
        
def IgnoreFudView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x98564E70c7fCC6d947fFE6d9EfeD5ba68b306F2E")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/4token.html", context)
        
def LfgswapView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0xF7a0b80681eC935d6dd9f3Af9826E68B99897d6D")
        resp = requests.get("https://app.geckoterminal.com/api/p1/core/pools/0xbb8502132c87ee31be0e2bc1cb8cc69374488261")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/lfgswap.html", context)

def LungView(request):
    if request.method == "POST":
        pass
    else:
        
        
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/0x28b9aed756de31b6b362aa0f23211d13093ebb79")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bsc/pools/0x0f008480ddc18b6bac65863dcd4ebbea0716e572")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/lung.html", context)
        
def BitgertView(request):
    if request.method == "POST":
        pass
    else:
        rs = requests.get("https://api.dexscreener.com/latest/dex/tokens/	0x8fff93e810a2edaafc326edee51071da9d398e83")
        resp = requests.get("https://app.geckoterminal.com/api/p1/bsc/pools/0x0f008480ddc18b6bac65863dcd4ebbea0716e572")
        getValue = resp.json()
        price_in_usd = getValue["data"]["attributes"]["price_in_usd"]
        fully_diluted_valuation = getValue["data"]["attributes"]["fully_diluted_valuation"]
        price_percent_change = getValue["data"]["attributes"]["price_percent_change"]
        from_volume_in_usd = getValue["data"]["attributes"]["from_volume_in_usd"]
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        liquidity = pairs["liquidity"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        fdv = pairs["fdv"]
        
        context = {"baseToken":baseToken,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd, "liquidity":liquidity, "txns":txns, "price_in_usd":price_in_usd, "fully_diluted_valuation":fully_diluted_valuation, "price_percent_change":price_percent_change, "from_volume_in_usd":from_volume_in_usd}
        return render(request, "main/bitgert.html", context)
        
def CantoView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=canto&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=canto&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        rs = requests.get("https://api.dexscreener.io/latest/dex/tokens/0x826551890dc65655a0aceca109ab11abdbd7a07b")
        dekatrons = rs.json()
        pairs = dekatrons["pairs"][0]
        baseToken = pairs["baseToken"]
        priceNative = pairs["priceNative"]
        priceUsd = pairs["priceUsd"]
        volume = pairs["volume"]
        txns = pairs["txns"]
        priceChange = pairs["priceChange"]
        volume = pairs["volume"]
        fdv = pairs["fdv"]
        price = str(response["canto"]["usd"])
        market_cap = int(response["canto"]["usd_market_cap"])
        hr_vol = str(response["canto"]["usd_24h_vol"])
        hr_chg = str(response["canto"]["usd_24h_change"])
        last_updated = str(response["canto"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,"priceNative":priceNative, "priceChange":priceChange, "volume":volume, "fdv":fdv, "volume":volume, "txns":txns, "priceUsd":priceUsd}
        return render(request, "main/canto.html", context)
        

        
def ComingView(request):
	if request.method == "POST":
		pass
		

	else:

		context = {}
		return render(request, "main/comingsoon.html", context)
        
def error_404(request, exception):
	return render(request,'app_user/400.html')
	
def error_500(request):
	return render(request,'app_user/500.html')

        
        
