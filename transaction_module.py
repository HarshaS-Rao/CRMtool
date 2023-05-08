from django.db import models

class Transaction(models.Model):
    account_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    account_holder = models.URLField(blank=True, null=True)
    motor_type = models.CharField(max_length=50, blank=True, null=True)
   
    def _str_(self):
        return self.name
        return self.email
