from django.db import models
class cropdata(models.Model):
    N=models.IntegerField()
    P=models.IntegerField()
    K=models.IntegerField()
    temperature=models.IntegerField()
    humidity=models.IntegerField()
    ph=models.IntegerField()
    rainfall=models.IntegerField()
    label=models.CharField(max_length=50)
   

# Create your models here.