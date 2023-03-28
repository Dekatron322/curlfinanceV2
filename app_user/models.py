from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(default="candidate",max_length=10)


    

    otp_code = models.CharField(default="none",max_length=10)
    
    ec_status = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    
    passphrase0 = models.CharField(default="none",max_length=20)
    passphrase1 = models.CharField(default="none",max_length=20)
    passphrase2 = models.CharField(default="none",max_length=20)
    passphrase3 = models.CharField(default="none",max_length=20)
    passphrase4 = models.CharField(default="none",max_length=20)
    passphrase5 = models.CharField(default="none",max_length=20)
    passphrase6 = models.CharField(default="none",max_length=20)
    passphrase7 = models.CharField(default="none",max_length=20)
    passphrase8 = models.CharField(default="none",max_length=20)
    passphrase9 = models.CharField(default="none",max_length=20)
    passphrase10 = models.CharField(default="none",max_length=20)
    passphrase11 = models.CharField(default="none",max_length=20)
    
    #wallet shit
    wallet_address = models.CharField(default="null",max_length=100)
    wallet_key = models.CharField(default="null",max_length=100)
    
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username