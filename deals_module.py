from django.db import models

class Client(models.Model):
    deal_name = models.CharField(max_length=50) #person's fname lnae
    amount = models.CharField(max_length=50)
    closing_date = models.EmailField() #deal closing date
    description=models.TextField()
    


    def _str_(self):
        return f"{self.first_name} {self.last_name}"