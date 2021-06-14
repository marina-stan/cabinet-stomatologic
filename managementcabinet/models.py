from django.db import models

class Person(models.Model):
   imagine = models.ImageField(upload_to='images', blank=True, null=True)
   nume_de_familie = models.CharField(max_length=255)
   prenume = models.CharField(max_length=255)
   cnp = models.CharField(max_length=255, default='')
   email = models.EmailField(max_length=254, default='', blank=True, null=True)
   numar_de_telefon = models.CharField(max_length=255, default='', blank=True, null=True)
   adresa = models.TextField(max_length=500, default='', blank=True, null=True)
   note = models.TextField(max_length=1500, default='', blank=True, null=True)
   status = models.BooleanField(default=True)

   def get_full_name(self):
       return self.nume_de_familie + " " + self.prenume

   def __str__(self):
       return self.nume_de_familie + " " + self.prenume + " - " + self.cnp

   class Meta:
       abstract = True


class Medic(Person):
    universitate = models.CharField(max_length=255, default='', blank=True, null=True)
    specializare = models.CharField(max_length=255, default='')
    data_absolvirii = models.DateField(blank=True, null=True)

    def permisiuni():
        return "medic"


class Asistent(Person):
    colegiu = models.CharField(max_length=255, default='', blank=True, null=True)
    specializare = models.CharField(max_length=255, default='', blank=True, null=True)
    data_absolvirii = models.DateField(blank=True, null=True)

    def permisiuni():
        return "asistent"


class Pacient(Person):
    persoana_de_contact = models.CharField(max_length=255, default='', blank=True, null=True)

    def permisiuni():
        return "pacient"


class Programare(models.Model):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE)
    asistent = models.ForeignKey(Asistent, on_delete=models.CASCADE)
    data_si_ora = models.DateTimeField()
    durata_in_minute = models.PositiveSmallIntegerField()
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)

    def preety_date_time(self):
        return self.data_si_ora.strftime("%Y-%m-%d, %H:%M")

    def __str__(self):
        return self.preety_date_time()  + " - " + self.pacient.nume_de_familie + " " + self.pacient.prenume


class Diagnostic(models.Model):
   denumire = models.CharField(max_length=255)
   notes = models.TextField(max_length=1500, default='', blank=True, null=True)
   status = models.BooleanField(default=True)

   def __str__(self):
       return self.denumire


class Partener(models.Model):
    denumire = models.CharField(max_length=255)
    tip_contract =  models.CharField(max_length=255, default='Furnizor', blank=True, null=True)
    valid_pana_la = models.DateField()
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.denumire


class Produs(models.Model):
    denumire = models.CharField(max_length=255)
    cantitate = models.PositiveSmallIntegerField()
    data_de_expirare = models.DateField()
    unitate_de_masura = models.CharField(max_length=255, default='buc', blank=True, null=True)
    distribuitor = models.ForeignKey(Partener, on_delete=models.CASCADE)
    pret_unitar = models.PositiveSmallIntegerField()
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.denumire

class Tratament(models.Model):
   denumire = models.CharField(max_length=255)
   produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
   cantitate = models.PositiveSmallIntegerField()
   notes = models.TextField(max_length=1500, default='', blank=True, null=True)
   status = models.BooleanField(default=True)

   def __str__(self):
       return self.denumire


class Factura(models.Model):
    numar_factura = models.PositiveSmallIntegerField()
    serie_factura =  models.CharField(max_length=20, default='SSD', blank=True, null=True)
    emitent = models.CharField(max_length=255, default='Cabinet stomatologic Smart Soft Dent')
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    cantitate = models.PositiveSmallIntegerField()
    tratament = models.ForeignKey(Tratament, on_delete=models.CASCADE)
    data_emitere = models.DateField()
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)

    def preety_date(self):
        return self.data_emitere.strftime("%Y-%m-%d")

    def __str__(self):
        return self.preety_date()  + " " + self.pacient.nume_de_familie + " " + self.pacient.prenume


class FisaPacient(models.Model):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    programare = models.ForeignKey(Programare, on_delete=models.CASCADE)
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
    tratament = models.ForeignKey(Tratament, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    notes = models.TextField(max_length=1500, default='', blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
      return self.pacient.nume_de_familie + " " + self.pacient.prenume + " " + self.pacient.cnp
