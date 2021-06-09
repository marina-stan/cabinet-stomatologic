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
    data_absolvirii = models.DateField()


class Asistent(Person):
    colegiu = models.CharField(max_length=255)
    specializare = models.CharField(max_length=255)
    data_absolvirii = models.DateField()


class Pacient(Person):
    persoana_de_contact = models.CharField(max_length=255)


class Programare(models.Model):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE)
    asistent = models.ForeignKey(Asistent, on_delete=models.CASCADE)
    data_si_ora = models.DateTimeField()
    durata_in_minute = models.PositiveSmallIntegerField()
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)


class Consultatie(models.Model):
    durata_in_minute = models.PositiveSmallIntegerField()
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)


class Diagnostic(models.Model):
   denumire = models.CharField(max_length=255)
   notes = models.TextField(max_length=1500, default='', blank=True, null=True)
   status = models.BooleanField(default=True)


class Partener(models.Model):
    denumire = models.CharField(max_length=255)
    tip_contract =  models.CharField(max_length=255, default='Furnizor', blank=True, null=True)
    valid_pana_la = models.DateField()
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)


class Produs(models.Model):
    denumire = models.CharField(max_length=255)
    cantitate = models.PositiveSmallIntegerField()
    data_de_expirare = models.DateField()
    unitate_de_masura = models.CharField(max_length=255, default='buc', blank=True, null=True)
    distribuitor = models.ForeignKey(Partener, on_delete=models.CASCADE)
    pret = models.FloatField()
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)


class Tratament(models.Model):
   denumire = models.CharField(max_length=255)
   produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
   cantitate = models.FloatField(default='1')
   notes = models.TextField(max_length=1500, default='', blank=True, null=True)
   status = models.BooleanField(default=True)


class Factura(models.Model):
    numar_factura = models.SmallIntegerField()
    serie_factura =  models.CharField(max_length=20, default='SSD', blank=True, null=True)
    emitent = models.CharField(max_length=255, default='Cabinet stomatologic Smart Soft Dent')
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    cantitate = models.FloatField()
    pret_unitar = models.FloatField()
    tratament = models.ForeignKey(Tratament, on_delete=models.CASCADE)
    data_emitere = models.DateField()
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)


class FisaPacient(models.Model):
   pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
   programare = models.ForeignKey(Programare, on_delete=models.CASCADE)
   consultatie = models.ForeignKey(Consultatie, on_delete=models.CASCADE)
   diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
   tratament = models.ForeignKey(Tratament, on_delete=models.CASCADE)
   factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
   notes = models.TextField(max_length=1500, default='', blank=True, null=True)
   status = models.BooleanField(default=True)
