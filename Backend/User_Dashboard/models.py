from django.db import models

# Create your models here.
class ecnomic_condition(models.Model):
    condition_name=models.CharField(max_length=10)
    lower_limit=models.IntegerField()
    upper_limit = models.IntegerField()

    def __str__(self):
        return self.condition_name

class user(models.Model):
    user_id=models.CharField(primary_key="TRUE",max_length=20)
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    user_economic_cond=models.ForeignKey(ecnomic_condition, on_delete=models.CASCADE)
    home_location = models.CharField(max_length=200)  # TODO Location Here
    email_id=models.EmailField()
    phone_no=models.IntegerField()
    insurance_status=models.BooleanField()

    def __str__(self):
        return self.user_name
