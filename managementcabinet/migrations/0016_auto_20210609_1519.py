# Generated by Django 2.2.24 on 2021-06-09 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managementcabinet', '0015_auto_20210609_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistent',
            old_name='address',
            new_name='adresa',
        ),
        migrations.RenameField(
            model_name='asistent',
            old_name='id_no',
            new_name='cnp',
        ),
        migrations.RenameField(
            model_name='asistent',
            old_name='college',
            new_name='colegiu',
        ),
        migrations.RenameField(
            model_name='asistent',
            old_name='graduation_date',
            new_name='data_absolvirii',
        ),
        migrations.RenameField(
            model_name='asistent',
            old_name='image',
            new_name='imagine',
        ),
        migrations.RenameField(
            model_name='asistent',
            old_name='notes',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='asistent',
            old_name='phone_no',
            new_name='numar_de_telefon',
        ),
        migrations.RenameField(
            model_name='asistent',
            old_name='first_name',
            new_name='nume_de_familie',
        ),
        migrations.RenameField(
            model_name='asistent',
            old_name='last_name',
            new_name='prenume',
        ),
        migrations.RenameField(
            model_name='asistent',
            old_name='specialization',
            new_name='specializare',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='address',
            new_name='adresa',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='id_no',
            new_name='cnp',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='graduation_date',
            new_name='data_absolvirii',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='image',
            new_name='imagine',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='notes',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='phone_no',
            new_name='numar_de_telefon',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='first_name',
            new_name='nume_de_familie',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='last_name',
            new_name='prenume',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='specialization',
            new_name='specializare',
        ),
        migrations.RenameField(
            model_name='medic',
            old_name='university',
            new_name='universitate',
        ),
        migrations.RenameField(
            model_name='pacient',
            old_name='address',
            new_name='adresa',
        ),
        migrations.RenameField(
            model_name='pacient',
            old_name='id_no',
            new_name='cnp',
        ),
        migrations.RenameField(
            model_name='pacient',
            old_name='image',
            new_name='imagine',
        ),
        migrations.RenameField(
            model_name='pacient',
            old_name='notes',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='pacient',
            old_name='phone_no',
            new_name='numar_de_telefon',
        ),
        migrations.RenameField(
            model_name='pacient',
            old_name='contact_person',
            new_name='nume_de_familie',
        ),
        migrations.RenameField(
            model_name='pacient',
            old_name='first_name',
            new_name='persoana_de_contact',
        ),
        migrations.RenameField(
            model_name='pacient',
            old_name='last_name',
            new_name='prenume',
        ),
    ]