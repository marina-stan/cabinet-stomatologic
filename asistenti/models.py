from django.db import models

class Asistent(models.Model):
    image = models.ImageField(upload_to='images/')
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    id_no = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    graduation_date = models.DateTimeField()
    notes = models.CharField(max_length=1200)
    status = models.CharField(max_length=200)
