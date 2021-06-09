from django.db import models

class Pacient(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    id_no = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    notes = models.CharField(max_length=1200)
    status = models.CharField(max_length=200)
