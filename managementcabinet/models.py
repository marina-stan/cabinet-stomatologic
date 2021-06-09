from django.db import models

class Medic(models.Model):
    image = models.ImageField(upload_to='images/')
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    id_no = models.CharField(max_length=200, default='', blank=True, null=True)
    email = models.CharField(max_length=200, default='', blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    university = models.CharField(max_length=200, default='', blank=True, null=True)
    specialization = models.CharField(max_length=200, default='', blank=True, null=True)
    graduation_date = models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=1200, default='', blank=True, null=True)
    status = models.CharField(max_length=200, default='', blank=True, null=True)
