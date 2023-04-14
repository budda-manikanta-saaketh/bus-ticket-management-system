from django.db import models

class Ticket(models.Model):
    full_name=models.CharField(max_length=50,null=True)
    aadhar_num=models.CharField(max_length=50,null=True) 
    From=models.CharField(max_length=50,null=True)
    To=models.CharField(max_length=50,null=True)
    date=models.DateField(max_length=50,null=True)
    no_of_seats=models.IntegerField(null=True)
    username=models.CharField(max_length=50,null=True)
    price=models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.full_name