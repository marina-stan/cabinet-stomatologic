# Generated by Django 2.2.24 on 2021-06-09 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managementcabinet', '0007_auto_20210609_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistent',
            name='status',
        ),
        migrations.RemoveField(
            model_name='medic',
            name='status',
        ),
    ]