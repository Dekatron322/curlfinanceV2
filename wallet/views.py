from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from app_user.models import AppUser
import requests

# Create your views here.


def RayGetName(wallet_address):
    resp = requests.get("http://api.iotexchartapp.com/bns/get-name/%s/" % str(wallet_address), verify=False).json()
    return resp


def RayGetAddress(domain_name):
    resp = requests.get("https://api.aibra.io/bns/get-address/%s/" % (domain_name)).json()
    return resp

@login_required(login_url='/app/sign-in/')
def CoreView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/coredao-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/coredao-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		print(data)
		#brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"app_user": app_user,  "total": total, "data": data,}
		return render(request, "wallet/index.html", context )

@login_required(login_url='/app/sign-in/')
def ProfileView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/loop-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/loop-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		print(data)
		#brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"app_user": app_user,  "total": total, "data": data,}
		return render(request, "wallet/profile.html", context )


		
@login_required(login_url='/app/sign-in/')
def SendView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		try:
			resp = requests.post("https://api.iotexchartapp.com/send-loop/", data={"sender": sender,"sender_key": sender_key, "receiver": receiver, "amount": amount, "token_address": token_address})
			SendB(sender, sender_key, receiver, amount, token)
			messages.warning(request, "Success: %s" % (txn_hash))
			return HttpResponseRedirect(reverse("wallet:index"))
		except:
			messages.warning(request, "Not successfully")
			return HttpResponseRedirect(reverse("wallet:index"))
				
				
		
	else:
		
		
		
		context = {"app_user": app_user}
		return render(request, "wallet/withdraw.html", context)
		
@login_required(login_url='/app/sign-in/')
def SendTokenView(request, token_address):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		
		if token_address == "0x27b45bCC26e01Ed50B4080A405D1c492FEe89d63":
			token = "doken"
		
		elif token_address == "0xeA8686a739550d9C88FaEfb39aC6cb78B6288767":
			token = "candy"
		
		
		
		
			#name = "Brise"
		else:
			pass
		try:
			resp = requests.post("https://api.iotexchartapp.com/send-loop/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				#SendB(sender, sender_key, receiver, amount, token)
			txn_hash = resp["txn_hash"]
			messages.success(request, (txn_hash))
			return HttpResponseRedirect(reverse("wallet:wallet"))
		except Exception as e:
			messages.warning(request, "Not successfull out of Gas")
				#print e
			return HttpResponseRedirect(reverse("wallet:wallet"))
		
	else:
		resp = requests.get("https://api.iotexchartapp.com/loop-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		if token_address == "0x27b45bCC26e01Ed50B4080A405D1c492FEe89d63":
			token = "doken"
			token_name = "Doken"
			brise_balance = data[0]["balance"]
			token_logo = data[0]["logo"]
		
		elif token_address == "0xeA8686a739550d9C88FaEfb39aC6cb78B6288767":
			token = "candy"
			token_name = "Candy Swap"
			brise_balance = data[1]["balance"]
			token_logo = data[1]["logo"]
		
		
		context = {"app_user": app_user, "token":token, "token_name":token_name, "brise_balance":brise_balance, "token_logo":token_logo, "data":data}
		return render(request, "wallet/send_token.html", context)
		
@login_required(login_url='/app/sign-in/')
def BitriseView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	
	domain_name = str(RayGetName("%s" % str(request.user.username))["names"])
	if len(domain_name) > 0:
	    domain_name = domain_name[2:-2].split("'")[-1]
	else:
	    domain_name = None
	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/bitrise-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/bitrise-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		print(data)
		#brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"domain_name": domain_name, "app_user": app_user,  "total": total, "data": data,}
		return render(request, "wallet/bitrise.html", context )
		
@login_required(login_url='/app/sign-in/')
def CantoView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/canto-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/canto-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		print(data)
		#brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"app_user": app_user,  "total": total, "data": data,}
		return render(request, "wallet/canto.html", context )
		
@login_required(login_url='/app/sign-in/')
def DokenView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/loop-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/loop-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		print(data)
		#brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"app_user": app_user,  "total": total, "data": data,}
		return render(request, "wallet/core.html", context )
		
@login_required(login_url='/app/sign-in/')
def SendBitriseTokenView(request, token_address):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	
	domain_name = str(RayGetName("%s" % str(request.user.username))["names"])
	if len(domain_name) > 0:
	    domain_name = domain_name[2:-2].split("'")[-1]
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		
		if receiver[0:2] != "0x":
		    receiver = RayGetAddress(receiver.replace(".brise", ""))
            #	print("sdsd sd s ds  ds dsdsd s d s s ds d sd")
            #print(receiver)
		
		if token_address == "0x8fff93e810a2edaafc326edee51071da9d398e83":
			token = "bitrise-token"
		
		elif token_address == "0xB999Ea90607a826A3E6E6646B404c3C7d11fa39D":
			token = "ice"
		elif token_address == "0x71946a5C9dA7C95ee804a9BE561EC15A3F286A7D":
			token = "brisepad"
		elif token_address == "0x5d4685c2C75581C67b9D6292A065a767bC214681":
		    token = "omniaverse"
		elif token_address == "0x9F7Bb6E8386ac9ad5e944d66fBa80F3F7231FA94":
		    token = "abr"
		elif token_address == "0x31226B28add9062c5064a9Bd35eA155F323C6ca6":
			token = "bprd"
		elif token_address == "0xD6447d2fA919811c41a064bDbdaB1E281F8de9B2":
			token = "vefi"
		elif token_address == "0xF26006408112be347c23FDBa03F7bC3566519655":
			token = "bswap"
		elif token_address == "0x6718e47e74497d1564EE76d832309144b83Ef8E8":
			token = "numi"
		elif token_address == "0xc89fcd3E1CF5A355fc41E160d18BAC5f624610D4":
			token = "wmf"
		elif token_address == "0xeB18A16A08530b811523fA49310319809ac4c979":
			token = "drv"
		elif token_address == "0xDe14b85cf78F2ADd2E867FEE40575437D5f10c06":
			token = "tether"
		elif token_address == "0xcf2DF9377A4e3C10e9EA29fDB8879d74C27FCDE7":
			token = "usdc-coin"
		elif token_address == "0x267Ae4bA9CE5ef3c87629812596b0D89EcBD81dD":
		    token = "evo-finance"
		elif token_address == "0x0e11DCE06eF2FeD6f78CEF5144F970E1184b4298":
		    token = "sphynx-labs"
		elif token_address == "0x38EA4741d100cAe9700f66B194777F31919142Ee":
		    token = "tokyo"
		elif token_address == "0x9b8535Dd9281e48484725bC9Eb6Ed2f66CEA2a36":
		    token = "zilla"
		elif token_address == "0xc3b730dD10A7e9A69204bDf6cb5A426e4f1F09E3":
		    token = "lung"
		elif token_address == "0x11203a00a9134Db8586381C4B2fca0816476b3FD":
		    token = "prt"
		elif token_address == "0xb860eCD8400600c13342a751408737235E177077":
		    token = "graphen"
	    
			#name = "Brise"
		else:
			pass
		try:
			resp = requests.post("https://api.iotexchartapp.com/send-bitrise/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				#SendB(sender, sender_key, receiver, amount, token)
			txn_hash = resp["txn_hash"]
			messages.success(request, (txn_hash))
			return HttpResponseRedirect(reverse("wallet:bitrise_wallet"))
		except Exception as e:
			messages.warning(request, "Not successfull out of Gas")
				#print e
			return HttpResponseRedirect(reverse("wallet:bitrise_wallet"))
		
	else:
		resp = requests.get("https://api.iotexchartapp.com/bitrise-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		if token_address == "0x8fff93e810a2edaafc326edee51071da9d398e83":
			token = "bitrise-token"
			token_name = "Wrapped Brise"
			brise_balance = data[0]["balance"]
			token_logo = data[0]["logo"]
		
		elif token_address == "0xB999Ea90607a826A3E6E6646B404c3C7d11fa39D":
			token = "ice"
			token_name = "Ice Cream"
			brise_balance = data[1]["balance"]
			token_logo = data[1]["logo"]
			
		elif token_address == "0x71946a5C9dA7C95ee804a9BE561EC15A3F286A7D":
			token = "brisepad"
			token_name = "BrisePad"
			brise_balance = data[2]["balance"]
			token_logo = data[2]["logo"]
			
		elif token_address == "0x5d4685c2C75581C67b9D6292A065a767bC214681":
		    token = "omniaverse"
		    token_name = "OmniaVerse"
		    brise_balance = data[3]["balance"]
		    token_logo = data[3]["logo"]
		    
		elif token_address == "0x9F7Bb6E8386ac9ad5e944d66fBa80F3F7231FA94":
		    token = "abr"
		    token_name = "Aibra"
		    brise_balance = data[4]["balance"]
		    token_logo = data[4]["logo"]
		
		
			
		elif token_address == "0x31226B28add9062c5064a9Bd35eA155F323C6ca6":
			token = "bprd"
			token_name = "Brise Paradise"
			brise_balance = data[5]["balance"]
			token_logo = data[5]["logo"]
		
		elif token_address == "0xD6447d2fA919811c41a064bDbdaB1E281F8de9B2":
			token = "vefi"
			token_name = "Vefi Ecosystem Token"
			brise_balance = data[6]["balance"]
			token_logo = data[6]["logo"]
			
		elif token_address == "0xF26006408112be347c23FDBa03F7bC3566519655":
			token = "bswap"
			token_name = "BriseSwap"
			brise_balance = data[7]["balance"]
			token_logo = data[7]["logo"]
			
		elif token_address == "0x6718e47e74497d1564EE76d832309144b83Ef8E8":
			token = "numi"
			token_name = "Numitor"
			brise_balance = data[8]["balance"]
			token_logo = data[8]["logo"]
			
		elif token_address == "0xc89fcd3E1CF5A355fc41E160d18BAC5f624610D4":
			token = "wmf"
			token_name = "Whale Maker Fund"
			brise_balance = data[9]["balance"]
			token_logo = data[9]["logo"]
		
		elif token_address == "0xeB18A16A08530b811523fA49310319809ac4c979":
			token = "drv"
			token_name = "Darrival"
			brise_balance = data[10]["balance"]
			token_logo = data[10]["logo"]
			
		#elif token_address == "0xeB18A16A08530b811523fA49310319809ac4c979":
			#token = "drv"
			#token_name = "Darrival"
			##brise_balance = data[11]["balance"]
			#token_logo = data[11]["logo"]
			
		elif token_address == "0xDe14b85cf78F2ADd2E867FEE40575437D5f10c06":
			token = "tether"
			token_name = "Tether USDT"
			brise_balance = data[11]["balance"]
			token_logo = data[11]["logo"]
			
		elif token_address == "0xcf2DF9377A4e3C10e9EA29fDB8879d74C27FCDE7":
			token = "usdc-coin"
			token_name = "USDC"
			brise_balance = data[12]["balance"]
			token_logo = data[12]["logo"]
		elif token_address == "0x267Ae4bA9CE5ef3c87629812596b0D89EcBD81dD":
		    token = "evo-finance"
		    token_name = "Evo Finance"
		    brise_balance = data[13]["balance"]
		    token_logo = data[13]["logo"]
		elif token_address == "0x0e11DCE06eF2FeD6f78CEF5144F970E1184b4298":
		    token = "sphynx-labs"
		    token_name = "Sphynx Lab"
		    brise_balance = data[14]["balance"]
		    token_logo = data[14]["logo"]
		elif token_address == "0x38EA4741d100cAe9700f66B194777F31919142Ee":
		    token = "tokyo"
		    token_name = "Toyko"
		    brise_balance = data[15]["balance"]
		    token_logo = data[15]["logo"]
		elif token_address == "0x9b8535Dd9281e48484725bC9Eb6Ed2f66CEA2a36":
		    token = "zilla"
		    token_name = "BriseZilla"
		    brise_balance = data[16]["balance"]
		    token_logo = data[16]["logo"]
		elif token_address == "0xc3b730dD10A7e9A69204bDf6cb5A426e4f1F09E3":
		    token = "lung"
		    token_name = "Lunagens"
		    brise_balance = data[17]["balance"]
		    token_logo = data[17]["logo"]
		elif token_address == "0x11203a00a9134Db8586381C4B2fca0816476b3FD":
		    token = "prt"
		    token_name = "Young Parrot"
		    brise_balance = data[18]["balance"]
		    token_logo = data[18]["logo"]
		elif token_address == "0xb860eCD8400600c13342a751408737235E177077":
		    token = "graphen"
		    token_name = "Graphen"
		    brise_balance = data[19]["balance"]
		    token_logo = data[19]["logo"]
		
		
		context = {"domain_name": domain_name, "app_user": app_user, "token":token, "token_name":token_name, "brise_balance":brise_balance, "token_logo":token_logo, "data":data}
		return render(request, "wallet/send_bitrise_token.html", context)
		
@login_required(login_url='/app/sign-in/')
def BscView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/bsc-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/bsc-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		print(data)
		#brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"app_user": app_user,  "total": total, "data": data,}
		return render(request, "wallet/bsc.html", context )
		
@login_required(login_url='/app/sign-in/')
def SendBscTokenView(request, token_address):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		
		if token_address == "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c":
			token = "bsc"
		
		elif token_address == "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82":
			token = "cake"
		
		elif token_address == "0xacFC95585D80Ab62f67A14C566C1b7a49Fe91167":
			token = "feg"
		
		elif token_address == "0xc748673057861a797275CD8A068AbB95A902e8de":
			token = "babydoge"
		
		elif token_address == "0x43a8a925c1930A313D283359184A64c51a2bc0E9":
			token = "navis"
		
		
		
			#name = "Brise"
		else:
			pass
		try:
			resp = requests.post("https://api.iotexchartapp.com/send-bsc/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				#SendB(sender, sender_key, receiver, amount, token)
			txn_hash = resp["txn_hash"]
			messages.success(request, (txn_hash))
			return HttpResponseRedirect(reverse("wallet:bsc_wallet"))
		except Exception as e:
			messages.warning(request, "Not successfull out of Gas")
				#print e
			return HttpResponseRedirect(reverse("wallet:bsc_wallet"))
		
	else:
		resp = requests.get("https://api.iotexchartapp.com/bsc-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		if token_address == "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c":
			token = "bsc"
			token_name = "BNB"
			brise_balance = data[0]["balance"]
			token_logo = data[0]["logo"]
		
		elif token_address == "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82":
			token = "cake"
			token_name = "Pancake"
			brise_balance = data[1]["balance"]
			token_logo = data[1]["logo"]
			
		elif token_address == "0xacFC95585D80Ab62f67A14C566C1b7a49Fe91167":
			token = "feg"
			token_name = "Feg Token"
			brise_balance = data[2]["balance"]
			token_logo = data[2]["logo"]
		
		elif token_address == "0xc748673057861a797275CD8A068AbB95A902e8de":
			token = "babydoge"
			token_name = "Babydoge"
			brise_balance = data[3]["balance"]
			token_logo = data[3]["logo"]
			
		elif token_address == "0x43a8a925c1930A313D283359184A64c51a2bc0E9":
			token = "navis"
			token_name = "Navis"
			brise_balance = data[4]["balance"]
			token_logo = data[4]["logo"]
		
		
		context = {"app_user": app_user, "token":token, "token_name":token_name, "brise_balance":brise_balance, "token_logo":token_logo, "data":data}
		return render(request, "wallet/send_bsc_token.html", context)
		

@login_required(login_url='/app/sign-in/')
def SendCoreTokenView(request, token_address):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		
		if token_address == "0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f":
			token = "core"
		
		elif token_address == "0xc0E49f8C615d3d4c245970F6Dc528E4A47d69a44":
			token = "ice"
		elif token_address == "0xf7a0b80681ec935d6dd9f3af9826e68b99897d6d":
			token = "lfgswap"
		elif token_address == "0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5":
			token = "shadowswap"
		
		elif token_address == "0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4":
			token = "bow"
		
		
			#name = "Brise"
		else:
			pass
		try:
			resp = requests.post("https://api.iotexchartapp.com/send-coredao/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				#SendB(sender, sender_key, receiver, amount, token)
			txn_hash = resp["txn_hash"]
			messages.success(request, (txn_hash))
			return HttpResponseRedirect(reverse("wallet:core_wallet"))
		except Exception as e:
			messages.warning(request, "Not successfull out of Gas")
				#print e
			return HttpResponseRedirect(reverse("wallet:core_wallet"))
	
	else:
		resp = requests.get("https://api.iotexchartapp.com/coredao-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		if token_address == "0x40375C92d9FAf44d2f9db9Bd9ba41a3317a2404f":
			token = "core"
			token_name = "Core"
			brise_balance = data[0]["balance"]
			token_logo = data[0]["logo"]
		
		elif token_address == "0xf7a0b80681ec935d6dd9f3af9826e68b99897d6d":
			token = "lfgswap"
			token_name = "LFG Swap"
			brise_balance = data[1]["balance"]
			token_logo = data[1]["logo"]
			
		elif token_address == "0xc0E49f8C615d3d4c245970F6Dc528E4A47d69a44":
			token = "ice"
			token_name = "Ice Cream"
			brise_balance = data[2]["balance"]
			token_logo = data[2]["logo"]
		
		elif token_address == "0xddBa66C1eBA873e26Ac0215Ca44892a07d83aDF5":
			token = "shadowswap"
			token_name = "Shadow Swap"
			brise_balance = data[3]["balance"]
			token_logo = data[3]["logo"]
			
		elif token_address == "0x1a639e150d2210A4BE4a5F0857A9151B241E7AE4":
		    token = "bow"
		    token_name = "Bow"
		    brise_balance = data[4]["balance"]
		    token_logo = data[4]["logo"]
			
		context = {"app_user": app_user, "token":token, "token_name":token_name, "brise_balance":brise_balance, "token_logo":token_logo, "data":data}
		return render(request, "wallet/send_core_token.html", context)
		
@login_required(login_url='/app/sign-in/')
def SendCantoTokenView(request, token_address):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		
		if token_address == "0x826551890dc65655a0aceca109ab11abdbd7a07b":
			token = "canto"
		
		elif token_address == "0x4e71a2e537b7f9d9413d3991d37958c0b5e1e503":
			token = "note"
		elif token_address == "0x7264610A66EcA758A8ce95CF11Ff5741E1fd0455":
			token = "cinu"
		
		
		
		
			#name = "Brise"
		else:
			pass
		try:
			resp = requests.post("https://api.iotexchartapp.com/send-canto/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				#SendB(sender, sender_key, receiver, amount, token)
			txn_hash = resp["txn_hash"]
			messages.success(request, (txn_hash))
			return HttpResponseRedirect(reverse("wallet:bsc_wallet"))
		except Exception as e:
			messages.warning(request, "Not successfull out of Gas")
				#print e
			return HttpResponseRedirect(reverse("wallet:canto_wallet"))
		
	else:
		resp = requests.get("https://api.iotexchartapp.com/canto-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		if token_address == "0x826551890dc65655a0aceca109ab11abdbd7a07b":
			token = "canto"
			token_name = "Cnto"
			brise_balance = data[0]["balance"]
			token_logo = data[0]["logo"]
		
		elif token_address == "0x4e71a2e537b7f9d9413d3991d37958c0b5e1e503":
			token = "note"
			token_name = "Note"
			brise_balance = data[1]["balance"]
			token_logo = data[1]["logo"]
			
		elif token_address == "0x7264610A66EcA758A8ce95CF11Ff5741E1fd0455":
			token = "cinu"
			token_name = "Canto Inu"
			brise_balance = data[2]["balance"]
			token_logo = data[2]["logo"]
		
		
		context = {"app_user": app_user, "token":token, "token_name":token_name, "brise_balance":brise_balance, "token_logo":token_logo, "data":data}
		return render(request, "wallet/send_canto_token.html", context)
		
		
@login_required(login_url='/app/sign-in/')
def LungView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/lung-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/lung-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		print(data)
		#brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"app_user": app_user,  "total": total, "data": data,}
		return render(request, "wallet/lung.html", context )
		
@login_required(login_url='/app/sign-in/')
def SendLungTokenView(request, token_address):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		
		if token_address == "0x28b9aed756de31b6b362aa0f23211d13093ebb79":
			token = "lung"
		
		elif token_address == "0x9b5FAeA17Df9D5953F44C70CC1Db5226F17B30E3":
			token = "doink"
		
		
		
		
		
			#name = "Brise"
		else:
			pass
		try:
			resp = requests.post("https://api.iotexchartapp.com/send-lung/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				#SendB(sender, sender_key, receiver, amount, token)
			txn_hash = resp["txn_hash"]
			messages.success(request, (txn_hash))
			return HttpResponseRedirect(reverse("wallet:bsc_wallet"))
		except Exception as e:
			messages.warning(request, "Not successfull out of Gas")
				#print e
			return HttpResponseRedirect(reverse("wallet:canto_wallet"))
		
	else:
		resp = requests.get("https://api.iotexchartapp.com/lung-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		if token_address == "0xf51666bcb4B787DF919395258Fb1d9556F4E357B":
			token = "lung"
			token_name = "WLung"
			brise_balance = data[0]["balance"]
			token_logo = data[0]["logo"]
		
		elif token_address == "0x9b5FAeA17Df9D5953F44C70CC1Db5226F17B30E3":
			token = "doink"
			token_name = "Doink"
			brise_balance = data[1]["balance"]
			token_logo = data[1]["logo"]
			
	
		
		
		context = {"app_user": app_user, "token":token, "token_name":token_name, "brise_balance":brise_balance, "token_logo":token_logo, "data":data}
		return render(request, "wallet/send_lung_token.html", context)


def error_404(request, exception):
	return render(request,'app_user/400.html')
	
def error_500(request):
	return render(request,'app_user/500.html')		
		


