from django.db import models

# Create your models here.

class state(models.Model):
    state_name=models.CharField(max_length=20)

    def __str__(self):
        return self.state_name

class city(models.Model):
    city_name=models.CharField(max_length=20)
    pincode_init=models.IntegerField()

    def __str__(self):
        return self.city_name


class hospital_price_slab(models.Model):
    slab_name=models.CharField(max_length=10)

    def __str__(self):
        return self.slab_name


class department(models.Model):
    department_name=models.CharField(max_length=40)
    doctor_names=models.TextField()
    visiting_charges=models.IntegerField()  #ToDo Add Validation
    cabin_charge=models.IntegerField()  #ToDo Add Validation
    cabin_empty=models.IntegerField()  #ToDo Add Validation
    bed_general_charge = models.IntegerField()  # ToDo Add Validation
    bed_general_empty = models.IntegerField()  # ToDo Add Validation

    def __str__(self):
        return self.department_name

class doctors(models.Model):
    doctor_name=models.CharField(max_length=50)
    hospital_1 = models.ForeignKey(department, on_delete=models.CASCADE)
    #hospital_2 = models.ForeignKey(department, related_name='%(class)s_requests_created' )

    def __str__(self):
        return self.doctor_name


class hospital(models.Model):
    hospital_id=models.CharField(primary_key="True",max_length=20)
    city_or_town=models.ForeignKey(city, on_delete=models.CASCADE)
    pincode=models.IntegerField()
    price_slab=models.ForeignKey(hospital_price_slab, on_delete=models.CASCADE)
    location=models.CharField(max_length=100)  #TODO Location Here
    hospital_name=models.CharField(max_length=100)
    hospital_rating=models.IntegerField() #ToDo Add Validation 1-10
    department_1 = models.ForeignKey(department, on_delete=models.CASCADE)
    #department_2 = models.ForeignKey(department,  related_name='%(class)s_requests_created' )
    #department_3 = models.ForeignKey(department, related_name='%(class)s_requests_created' )
    #department_4 = models.ForeignKey(department, related_name='%(class)s_requests_created' )
    #department_5 = models.ForeignKey(department, related_name='%(class)s_requests_created' )
    #department_6 = models.ForeignKey(department, related_name='%(class)s_requests_created' )

    def __str__(self):
        return self.hospital_name
