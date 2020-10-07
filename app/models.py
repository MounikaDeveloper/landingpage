from django.db import models

# Create your models here.
class LandingFormModel(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    emailid=models.EmailField(max_length=50)
    mobile=models.PositiveBigIntegerField()
    message=models.CharField(max_length=200,default='OK')