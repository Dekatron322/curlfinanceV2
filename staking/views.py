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

# Create your views here.


def IndexView(request):
	if request.method == "POST":
		pass


	else:
	    context = {}
	    return render(request, "staking/index.html", context )


def StakeView(request):
	if request.method == "POST":
		pass


	else:
	    context = {}
	    return render(request, "staking/stake.html", context )


def HarvestView(request):
	if request.method == "POST":
		pass


	else:
	    context = {}
	    return render(request, "staking/harvest.html", context )