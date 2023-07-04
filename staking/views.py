from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
import requests
from app_user.models import AppUser
from staking.models import Stake
from launchpad.models import *

from datetime import datetime
import datetime as dt



# Create your views here.


def IndexView(request, ido_id):
	if request.method == "POST":
		pass


	else:
		context = {"ido_id": ido_id}
		return render(request, "staking/index.html", context )


def StakeView(request, ido_id, amount):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	ido = Ido.objects.get(id=ido_id)
	if request.method == "POST":
		duration = 30 #60

		bep_balance = requests.get("https://api.iotexchartapp.com/aibra/get-balance/%s/" % (app_user.wallet_address)).json()

		#return HttpResponse(str(float(bep_balance["data"][0]["balance"])))
		if float(float(bep_balance["data"][0]["balance"])) > amount:
			
			sender = app_user.wallet_address
			sender_key = app_user.wallet_key
			receiver = "0xbCA60DDe596B82a4Cb8CC3233BF8f0ED09280557"
			amount = amount
			token = "abr"
		
			try:
				resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				txn_hash = resp["txn_hash"]
				
			except:
				txn_hash = None
		
			if txn_hash != None:
				stake = Stake.objects.create(app_user=app_user, amount=amount, duration=duration)
				stake.save()

				returns = float(amount) + float(amount)*0.1 #25%
				returnsk = float(float(returns)*0.03) + float(float(amount)*0.01)
				returns = float(returns) - float(returnsk)
			
				stake.returns = returns

				payment_hash = txn_hash
				stake.payment_hash = payment_hash
				stake.payment_status = True
				stake.amount_tax = float(float(amount)*0.01)
				stake.returns_tax = float(float(returns)*0.03)
				stake.total_tax = returnsk
				stake.payment_confirmation_status = True
				

				today = timezone.now().date()
				due_date = today + dt.timedelta(days=int(duration))
				stake.due_date = due_date

				stake.save()

				if stake:
					ist = IdoStakeConnector(ido=ido, stake=stake)
					ist.save()

				messages.warning(request, "Congratulations! you have successfully staked your asset! %s" % (txn_hash))
				return HttpResponseRedirect(reverse("stake:my_stakes"))

			else:
				messages.warning(request, "Sorry!! your staking could not go through.(Try top-up your account.._")
				return HttpResponseRedirect(reverse("stake:my_stakes"))

		else:
				messages.warning(request, "Sorry! something went wrong. (Try top-up your account.)")
				return HttpResponseRedirect(reverse("stake:my_stakes"))


	else:

		ido = Ido.objects.get(id=ido_id)
		staked_status = False
		for item in ido.stakes.all():
			if item.app_user == app_user:
				staked_status = True
				break;
		
		if staked_status:
			messages.warning(request, "Sorry! something went wrong. (You already staked.)")
			return HttpResponseRedirect(reverse("stake:my_stakes"))

		else:
			bep_balance = requests.get("https://api.iotexchartapp.com/aibra/get-balance/%s/" % (app_user.wallet_address)).json()
			curl_balance = float(float(bep_balance["data"][0]["balance"]))
			context = {"app_user": app_user, "curl_balance":curl_balance}
			return render(request, "staking/stake.html", context)


def HarvestView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "staking/harvest.html", context )
	

def MyStakesView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/brise-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()

		my_stakes = Stake.objects.filter(app_user=app_user).order_by('-pub_date')
		
		from datetime import datetime
		if len(my_stakes) > 0:
			stake = my_stakes.last()
			last_date = datetime(int(str(stake.due_date)[:4]), int(str(stake.due_date)[5:7]), int(str(stake.due_date)[8:10]))
			launch_date = datetime(2022, 8, 16)
			if last_date > launch_date or last_date == launch_date:
				return_checker = "10%"
			else:
				return_checker = "25%"
			#return HttpResponse(str(launch_date))
		else:
			return_checker = None
			
		

		context = {"my_stakes": my_stakes, "app_user": app_user, "wallet_address": app_user.wallet_address, "1_per": 0.01, "3_per": 0.03, "return_checker":return_checker}
		return render(request, "staking/my_stakes.html", context)
	


def HarvestView(request, stake_id):
	stake = Stake.objects.get(id=stake_id)
	app_user = AppUser.objects.get(user__pk=request.user.id)
	
	from datetime import datetime
	due_date = datetime(int(str(stake.due_date)[:4]), int(str(stake.due_date)[5:7]), int(str(stake.due_date)[8:10]))
	today_date = datetime.now()

	if today_date > due_date or today_date == due_date:
		ready = True
	else:
		ready = False

	if ready:

		sender = "0x545486DE665fb131F21bbEB1B6CAF1973Fc5258f"
		sender_key = "0x5629bdb8cba3d052638539c5073eed8ac9b08739f02e3f43076bb41de729cce1"
		receiver = app_user.wallet_address
		amount = stake.returns
		token = "abr"

		try:
			resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key": sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
			txn_hash = resp["txn_hash"]
			
		except:
			txn_hash = None

		if txn_hash:
			stake.harvested_status = True
			stake.save()

		messages.warning(request, "Harvest successful!")
		return HttpResponseRedirect(reverse("stake:my_stakes"))
	
	else:
		messages.warning(request, "Sorry! something went wrong. (Stake not due for harvest.)")
		return HttpResponseRedirect(reverse("stake:my_stakes"))
