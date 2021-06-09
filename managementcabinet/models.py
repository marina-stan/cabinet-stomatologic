from django.db import models

class Person(models.Model):
   imagine = models.ImageField(upload_to='images/%Y/%m/%d')
   nume_de_familie = models.CharField(max_length=255)
   prenume = models.CharField(max_length=255)
   cnp = models.CharField(max_length=255, default='', blank=True, null=True)
   email = models.EmailField(max_length=254, default='', blank=True, null=True)
   numar_de_telefon = models.CharField(max_length=255, default='', blank=True, null=True)
   adresa = models.TextField(max_length=500, default='', blank=True, null=True)
   note = models.TextField(max_length=1500, default='', blank=True, null=True)
   status = models.BooleanField(default=True)

   def get_full_name(self):
       return self.last_name, self.first_name

   class Meta:
       abstract = True


class Medic(Person):
    universitate = models.CharField(max_length=255, default='', blank=True, null=True)
    specializare = models.CharField(max_length=255, default='', blank=True, null=True)
    data_absolvirii = models.DateTimeField()


class Asistent(Person):
    colegiu = models.CharField(max_length=255)
    specializare = models.CharField(max_length=255)
    data_absolvirii = models.DateTimeField()


class Pacient(Person):
    persoana_de_contact = models.CharField(max_length=255)
