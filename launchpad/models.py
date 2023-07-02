from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from app_user.models import AppUser
from staking.models import Stake

# Create your models here.

class Contributor(models.Model):
    wallet_address = models.TextField(default="null")

    input_amount = models.FloatField(default=0)
    output_amount = models.FloatField(default=0)
    output_date = models.DateTimeField(default=timezone.now)

    ido_id = models.CharField(max_length=10, default="null")
    ewithdraw_status = models.BooleanField(default=False)
    claimed_status = models.BooleanField(default=False)

    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.wallet_address)


class White(models.Model):
    wallet_address = models.TextField(default="null")
    tier = models.CharField(max_length=20, default="null")

    input_amount = models.FloatField(default=0)
    output_amount = models.FloatField(default=0)
    output_date = models.DateTimeField(default=timezone.now)

    ido_id = models.CharField(max_length=10, default="null")
    ewithdraw_status = models.BooleanField(default=False)
    claimed_status = models.BooleanField(default=False)

    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.wallet_address)


class Ido(models.Model):
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True)

    logo = models.FileField(upload_to='account_files/logos/', blank=True, default="default_files/default_file.png")
    image = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    token_address = models.CharField(max_length=50, default="null")
    token_symbol = models.CharField(max_length=3, default="null")

    wallet_address = models.CharField(max_length=50, default="null")
    wallet_address_key = models.CharField(max_length=50, default="null")

    name = models.CharField(max_length=20, default="null")
    description = models.TextField(default="null")
    link = models.TextField(default="null")

    listing_price = models.FloatField(default=0)
    presale_price = models.FloatField(default=0)

    soft_cap = models.FloatField(default=0)
    hard_cap = models.FloatField(default=0)

    tier0_min = models.FloatField(default=0)
    tier1_min = models.FloatField(default=0)
    tier2_min = models.FloatField(default=0)
    tier3_min = models.FloatField(default=0)

    tier0_max = models.FloatField(default=0)
    tier1_max = models.FloatField(default=0)
    tier2_max = models.FloatField(default=0)
    tier3_max = models.FloatField(default=0)

    whitelist_limit = models.IntegerField(default=None, null=True)
    whitelist = models.ManyToManyField(White, through="IdoWhiteConnector")
    whitelist_start = models.DateTimeField(default=timezone.now)
    whitelist_stop = models.DateTimeField(default=timezone.now)
    
    contributors = models.ManyToManyField(Contributor, through="IdoContributorConnector")
    ido_start = models.DateTimeField(default=timezone.now)
    ido_stop = models.DateTimeField(default=timezone.now)

    stakes = models.ManyToManyField(Stake, through="IdoStakeConnector")

    allocation_cf_liquidity = models.FloatField(default=0)
    allocation_cf_project = models.FloatField(default=0)

    allocation_pt_liquidity = models.FloatField(default=0)
    allocation_pt_contributors = models.FloatField(default=0)
    allocation_pt_project = models.FloatField(default=0)

    withdraw_project_token_status = models.BooleanField(default=False)
    withdraw_contributed_token_status = models.BooleanField(default=False)

    total_supply = models.FloatField(default=0)
    
    vesting_duration = models.IntegerField(default=0)
    vesting_amount = models.FloatField(default=0)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class IdoWhiteConnector(models.Model):
	ido = models.ForeignKey(Ido, on_delete=models.CASCADE)
	whitelist = models.ForeignKey(White, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class IdoContributorConnector(models.Model):
	ido = models.ForeignKey(Ido, on_delete=models.CASCADE)
	contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)
        

class IdoStakeConnector(models.Model):
	ido = models.ForeignKey(Ido, on_delete=models.CASCADE)
	stake = models.ForeignKey(Stake, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)