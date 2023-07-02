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

from launchpad.models import *
from app_user.models import *

# Create your views here.


def CompareDatetimes(due_date):
	import pytz
	from datetime import datetime
	import datetime as dt
	utc = pytz.UTC
	#live datetime.now value might change
	#today_date = utc.localize(datetime.now())
	today_date = utc.localize(datetime.now()+ dt.timedelta(hours=1))
	due_date = due_date
		
	if today_date.replace(tzinfo=utc) >= due_date.replace(tzinfo=utc):
		running_status = False
	else:
		running_status = True

	print(running_status)
	print(today_date.replace(tzinfo=utc))
	print(due_date.replace(tzinfo=utc))
	print("shshdhdsdhshdshdshdhdhhsdhsdhshdhdhhshdhhd")

	return running_status


def AddIdoView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		listing_price = request.POST.get("listing_price")
		presale_price = request.POST.get("presale_price")

		token_address = request.POST.get("token_address")
		token_symbol = request.POST.get("token_symbol")

		total_supply = request.POST.get("total_supply")

		name = request.POST.get("name")
		description = request.POST.get("description")
		link = request.POST.get("link")
		soft_cap = request.POST.get("soft_cap")
		hard_cap = request.POST.get("hard_cap")

		tier0_min = request.POST.get("tier0_min")
		tier1_min = request.POST.get("tier1_min")
		tier2_min = request.POST.get("tier2_min")
		tier3_min = request.POST.get("tier3_min")

		tier0_max = request.POST.get("tier0_max")
		tier1_max = request.POST.get("tier1_max")
		tier2_max = request.POST.get("tier2_max")
		tier3_max = request.POST.get("tier3_max")

		whitelist_limit = request.POST.get("whitelist_limit")
		whitelist_start = request.POST.get("whitelist_start")
		whitelist_stop = request.POST.get("whitelist_stop")

		ido_start = request.POST.get("ido_start")
		ido_stop = request.POST.get("ido_stop")

		allocation_cf_liquidity = request.POST.get("allocation_cf_liquidity")
		allocation_cf_project = request.POST.get("allocation_cf_project")

		allocation_pt_liquidity = request.POST.get("allocation_pt_liquidity")
		allocation_pt_contributors = request.POST.get("allocation_pt_contributors")
		allocation_pt_project = request.POST.get("allocation_pt_project")

		vesting_duration = request.POST.get("vesting_duration")

		try:
			image = request.FILES["image"]
		except:
			image = None

		try:
			logo = request.FILES["logo"]
		except:
			logo = None

		ido = Ido.objects.create(app_user=app_user, listing_price=listing_price, presale_price=presale_price,
			   token_address=token_address, token_symbol=token_symbol, total_supply=total_supply,
			   name=name, description=description, link=link, soft_cap=soft_cap, hard_cap=hard_cap,
			tier0_min=tier0_min, tier1_min=tier1_min, tier2_min=tier2_min, tier3_min=tier3_min, 
			tier0_max=tier0_max, tier1_max=tier1_max, tier2_max=tier2_max, tier3_max=tier3_max,
			ido_start=ido_start, ido_stop=ido_stop, logo=logo, image=image,
			allocation_cf_liquidity=allocation_cf_liquidity, allocation_cf_project=allocation_cf_project,
			allocation_pt_liquidity=allocation_pt_liquidity, allocation_pt_contributors=allocation_pt_contributors, 
			allocation_pt_project=allocation_pt_project, vesting_duration=vesting_duration
			)
		ido.save()

		if whitelist_limit:
			ido.whitelist_limit = whitelist_limit
			ido.whitelist_start = whitelist_start
			ido.whitelist_stop = whitelist_stop
			ido.save()

		if ido:
			resp = requests.post("https://api.iotexchartapp.com/brise-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			ido.wallet_address = wallet_address
			ido.wallet_address_key = wallet_key
			ido.save()

		messages.warning(request, "Ido Created")
		return HttpResponseRedirect(reverse("launchpad:fund_presale", args=[ido.id]))


	else:
		context = {"app_user": app_user}
		return render(request, "launchpad/add_ido.html", context )




def FundPresaleView(request, ido_id):
	ido = Ido.objects.get(id=ido_id)
	if request.method == "POST":
		pass


	else:
		context = {"ido": ido}
		return render(request, "launchpad/fund_presale.html", context )



def IndexView(request):
	if request.method == "POST":
		pass


	else:
		idos = Ido.objects.all().order_by('-pub_date')[0:10]
		context = {"idos": idos}
		return render(request, "launchpad/index.html", context )


def DetailsView(request, ido_id):
	if request.method == "POST":
		pass


	else:
		ido = Ido.objects.get(id=ido_id)

		#check for whitelist status
		if ido.whitelist_limit:

			#check if staking is running
			running_status = CompareDatetimes(ido.whitelist_stop)
		else:
			running_status = CompareDatetimes(ido.ido_stop)

		#inactive(using whitelist filling model)
		#if ido.stakes.count() >= int(ido.whitelist_limit):
		#	whitelisting = False
		#else:
		#	whitelisting = True

		context = {"ido": ido, "whitelisting": running_status}
		return render(request, "launchpad/details.html", context )


def WithdrawIdoFund(request, amount):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	sender = app_user.wallet_address
	sender_key = app_user.wallet_key
	receiver = "0x545486DE665fb131F21bbEB1B6CAF1973Fc5258f" 
	token = "abr"

	try:
		resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key": sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
		txn_hash = resp["txn_hash"]
		
	except:
		txn_hash = None

	print(txn_hash)
	return txn_hash

def ContributeView(request, ido_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	ido = Ido.objects.get(id=ido_id)

	#getting the stake
	stake = None
	for item in ido.stakes.all():
		if item.app_user == app_user:
			stake = item
			break



	#generating the min and max for contribution
	if stake == None:
		tier_value = 0
		min_val = ido.tier0_min
		max_val = ido.tier0_max
	elif stake.amount == float(1):
		tier_value = 1
		min_val = ido.tier1_min
		max_val = ido.tier1_max
	elif stake.amount == float(2):
		tier_value = 2
		min_val = ido.tier2_min
		max_val = ido.tier2_max
	else:
		tier_value = 3
		min_val = ido.tier3_min
		max_val = ido.tier3_max

	if request.method == "POST":

		#check if user' contribution status
		contributed = False
		for item in ido.contributors.all():
			if item.wallet_address == app_user.wallet_address:
				contributed = True
				contributor = item
				break

		#check if user' whitelisted status
		whitelisted = False
		for item in ido.whitelist.all():
			if item.wallet_address == app_user.wallet_address:
				whitelisted = True
				white = item
				break
		
		if contributed == False and whitelisted == False:
			input_amount = float(request.POST.get("input_amount"))
			if WithdrawIdoFund(request, input_amount):
				output_amount = float(input_amount) * float(ido.presale_price)
				contributor = Contributor.objects.create(ido_id=ido.id, wallet_address=app_user.wallet_address, input_amount=input_amount,
							output_amount=output_amount)
				contributor.save()

				ic = IdoContributorConnector(ido=ido, contributor=contributor)
				ic.save()
			else:
				print("sorry withdrawal not sucessful")
				messages.warning(request, "Sorry, this is not successful")
				return HttpResponseRedirect(reverse("launchpad:launchpad"))

		elif whitelisted == True and contributed == False:
			input_amount = float(request.POST.get("input_amount"))
			if WithdrawIdoFund(request, input_amount):
				output_amount = float(input_amount) * float(ido.presale_price)
				white.input_amount += input_amount
				white.output_amount += output_amount

				#check for contribution cap(tier_max)
				if float(white.input_amount) + float(input_amount) > float(max_val):
					messages.warning(request, "Sorry, you will exceed your contribution limit")
					return HttpResponseRedirect(reverse("launchpad:launchpad"))
				
				else:
					white.save()

			else:
				print("sorry, this not sucessful")
				messages.warning(request, "Sorry, this is not successful")
				return HttpResponseRedirect(reverse("launchpad:launchpad"))

		elif contributed == True and whitelisted == False:
			
			input_amount = float(request.POST.get("input_amount"))
			if WithdrawIdoFund(request, input_amount):
				output_amount = float(input_amount) * float(ido.presale_price)
				contributor.input_amount += input_amount
				contributor.output_amount += output_amount

				#check for contribution cap(tier_max)
				if float(contributor.input_amount) + float(input_amount) > float(ido.tier0_max):
					messages.warning(request, "Sorry, you will exceed your contribution limit")
					return HttpResponseRedirect(reverse("launchpad:launchpad"))
				
				else:
					contributor.save()
			else:
				print("sorry not sucessfull")
				messages.warning(request, "Sorry, this is not successful")
				return HttpResponseRedirect(reverse("launchpad:launchpad"))

		else:
			input_amount = float(request.POST.get("input_amount"))
			if WithdrawIdoFund(request, input_amount):
				output_amount = float(input_amount) * float(ido.presale_price)
				white = White.objects.create(ido_id=ido.id, wallet_address=app_user.wallet_address, input_amount=input_amount,
							output_amount=output_amount)
				white.save()

				iw = IdoWhiteConnector(ido=ido, white=white)
				iw.save()

			else:
				print("sorry not sucess")
				messages.warning(request, "Sorry, this is not successful")
				return HttpResponseRedirect(reverse("launchpad:launchpad"))


		messages.warning(request, "Contribution completed!")
		return HttpResponseRedirect(reverse("launchpad:launchpad"))



	else:


		if ido.whitelist_limit:
			#check if staking is running
			running_status = CompareDatetimes(ido.whitelist_stop)

			if running_status == False:

			#checking if whitelist is filled(active)
			#if ido.stakes.count() >= ido.whitelist_limit:

				#check if presale is running
				running_status = CompareDatetimes(ido.ido_stop)

				if running_status == False:
					contributions = 0
					for item in ido.contributors.all():
						contributions += float(item.input_amount)

					if contributions != 0:
						progress = contributions/float(ido.hard_cap) * 100
						#progress = float(float(ido.soft_cap)/contributions) * 100
					else:
						progress = 0

					context = {"app_user": app_user, "ido": ido, "progress": progress,
				"contributions": contributions, "min_val": int(min_val), "max_val": int(max_val)}
					return render(request, "launchpad/contribute.html", context )
				
				else:
					
					messages.warning(request, "Sorry, presale is no longer runnning.")
					return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))
				
			else:
				print("debuggingggggggggggggggggg")
				messages.warning(request, "Staking pool is open for this presale")
				return HttpResponseRedirect(reverse("stake:pool", args=[ido.id]))
			
		else:
			#check if presale is running
			running_status = CompareDatetimes(ido.ido_stop)

			if running_status:
				contributions = 0
				for item in ido.contributors.all():
					contributions += float(item.input_amount)

				if contributions != 0:
					progress = contributions/float(ido.hard_cap) * 100
					#progress = float(float(ido.soft_cap)/contributions) * 100
				else:
					progress = 0

				context = {"app_user": app_user, "ido": ido, "progress": progress,
			"contributions": contributions, "min_val": int(min_val), "max_val": int(max_val)}
				return render(request, "launchpad/contribute.html", context )
			
			else:
				messages.warning(request, "Sorry, presale is no longer runnning.")
				return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))
			

def MyPresalesView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "launchpad/my_presales.html", context )
	

def MyIdosView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		idos = Ido.objects.filter(app_user=app_user).order_by('-pub_date')[0:10]
		context = {"idos": idos}
		return render(request, "launchpad/my_idos.html", context )
	

def MyContributionsView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		whitelist = White.objects.filter(wallet_address=app_user.wallet_address)
		contributions = Contributor.objects.filter(wallet_address=app_user.wallet_address)

		contribs = []
		for item in whitelist:
			contribs.append(item)
		
		for item in contributions:
			contribs.append(item)

		#getting all contributions
		result = []
		for item in contribs:
			ido = Ido.objects.get(id=int(item.ido_id))
			val = {
				"contribution": item,
				"ido": ido
			}
			result.append(val)

		context = {"result": result}
		return render(request, "launchpad/my_contributions.html", context )
	


def ClaimView(request, ido_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	ido = Ido.objects.get(id=ido_id) #ido_start #whitelist_start

	running_status = CompareDatetimes(ido.ido_stop)
	if running_status == False:

		#declaring defaults
		contributor = None
		white = None
		contribution = None

		######check for whitelist status and contribution
		#check if user' contribution status
		contributed = False
		for item in ido.contributors.all():
			if item.wallet_address == app_user.wallet_address:
				contributed = True
				contributor = item
				break

		#check if user' whitelisted status
		whitelisted = False
		for item in ido.whitelist.all():
			if item.wallet_address == app_user.wallet_address:
				whitelisted = True
				white = item
				break


		if contributed:
			contribution = contributor

		elif whitelisted:
			contribution = white

		else:
			contribution = None

		#check if user already claimed
		if contribution.claimed_status == False:
			#withdrawing output_amount from contribution
			sender = ido.wallet_address # "0x545486DE665fb131F21bbEB1B6CAF1973Fc5258f"
			sender_key = ido.wallet_address_key # "0x5629bdb8cba3d052638539c5073eed8ac9b08739f02e3f43076bb41de729cce1"
			receiver = app_user.wallet_address
			amount = contribution.output_amount
			token = ido.token_symbol

			try:
				resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key": sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				txn_hash = resp["txn_hash"]
				
			except:
				txn_hash = None

			print(txn_hash)
			if txn_hash:
				contribution.claimed_status = True
				contribution.save()
				messages.warning(request, "Claim successful!")
				return HttpResponseRedirect(reverse("launchpad:my_contributions"))
			
			else:
				messages.warning(request, "Claim not successful!")
				return HttpResponseRedirect(reverse("launchpad:my_contributions"))
			
		else:
			messages.warning(request, "Claim not successful!, You already claimed your tokens!")
			return HttpResponseRedirect(reverse("launchpad:my_contributions"))
		
	else:
		messages.warning(request, "Claim not successful!, Presale is still running!")
		return HttpResponseRedirect(reverse("launchpad:my_contributions"))


def EWithdrawView(request, ido_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	ido = Ido.objects.get(id=ido_id) #ido_start #whitelist_start

	#declaring defaults
	contributor = None
	white = None

	######check for whitelist status and contribution
	#check if user' contribution status
	contributed = False
	for item in ido.contributors.all():
		if item.wallet_address == app_user.wallet_address:
			contributed = True
			contributor = item
			break

	#check if user' whitelisted status
	whitelisted = False
	for item in ido.whitelist.all():
		if item.wallet_address == app_user.wallet_address:
			whitelisted = True
			white = item
			break

	######

	if contributed:
		contribution = contributor
		max_output = contributor.input_amount

	elif whitelisted:
		contribution = white
		max_output = white.input_amount

	else:
		contribution = None
		max_output = None

	if request.method == "POST":
		#getting amount for withdrawl
		amount = request.POST.get("amount")
		
		#check if presale is running
		running_status = CompareDatetimes(ido.ido_stop)

		if running_status == False:

			if contribution:
				sender = "0x545486DE665fb131F21bbEB1B6CAF1973Fc5258f"
				sender_key = "0x5629bdb8cba3d052638539c5073eed8ac9b08739f02e3f43076bb41de729cce1"
				receiver = app_user.wallet_address
				amount = contribution.output_amount
				token = "abr"

				try:
					resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key": sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
					txn_hash = resp["txn_hash"]
					
				except:
					txn_hash = None

				if txn_hash and contributed:
					contributor.ewithdraw_status = True
					contributor.save()

				else:
					white.ewithdraw_status = True
					white.save()

				
				messages.warning(request, "Withdrawal successful!")
				return HttpResponseRedirect(reverse("lauchpad:details", args=[ido.id]))
			
			else:
				messages.warning(request, "Sorry! something went wrong. (You didnt invest yet!)")
				return HttpResponseRedirect(reverse("lauchpad:details", args=[ido.id]))

		else:
			messages.warning(request, "Sorry! something went wrong. (Presale is over, you can no longer withdraw)")
			return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))

	else:
		print(max_output)
		context = {"max_output": max_output}
		return render(request, "launchpad/e_withdraw.html", context )
	

def EndPresaleView(request):
	pass
	


def WithdrawPtView(request, ido_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	ido = Ido.objects.get(id=ido_id) 

	running_status = CompareDatetimes(ido.ido_stop)
	if running_status == False:
		sender = ido.wallet_address
		sender_key = ido.wallet_address_key 
		receiver = app_user.wallet_address
		amount = float((ido.allocation_pt_project/100) * ido.total_supply)
		token = ido.token_symbol

		try:
			resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key": sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
			txn_hash = resp["txn_hash"]
			
		except:
			txn_hash = None

		if txn_hash:
			ido.withdraw_project_token_status = True
			ido.save()

			messages.warning(request, "Success. (Withdraw completed)")
			return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))

		else:
			messages.warning(request, "Sorry! something went wrong. (Withdraw not completed)")
			return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))


	else:
		messages.warning(request, "Sorry! something went wrong. (Presale is not over yet.)")
		return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))



def WithdrawCtView(request, ido_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	ido = Ido.objects.get(id=ido_id) 

	running_status = CompareDatetimes(ido.ido_stop)
	if running_status == False:
		if ido.vesting_duration > 0:

			contributions = 0
			for item in ido.whitelist.all():
				contributions += item.input_amount

			for item in ido.contributors.all():
				contributions += item.input_amount

			#amount that can be withdrawn
			removable = contributions/ido.vesting_duration

			#check for previous withdraw
			if ido.vesting_amount == 0:
				ido.vesting_amount = removable
				ido.save()

			sender = ido.wallet_address
			sender_key = ido.wallet_address_key 
			receiver = app_user.wallet_address
			amount = ido.vesting_amount
			token = "abr"

			try:
				resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key": sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				txn_hash = resp["txn_hash"]
				
			except:
				txn_hash = None

			if txn_hash:
				ido.withdraw_contributed_token_status = True
				ido.vesting_duration -= 1
				ido.save()
				

				messages.warning(request, "Success. (Withdraw completed)")
				return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))

			else:
				messages.warning(request, "Sorry! something went wrong. (Withdraw not completed)")
				return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))
			
		else:
			messages.warning(request, "Sorry! Withdrawal Completed/Didnt Select Vesting)")
			return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))


	else:
		messages.warning(request, "Sorry! something went wrong. (Presale is not over yet.)")
		return HttpResponseRedirect(reverse("launchpad:details", args=[ido.id]))