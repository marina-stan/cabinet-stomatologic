# Generated by Django 2.2.24 on 2021-06-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementcabinet', '0005_auto_20210609_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistent',
            name='status',
            field=models.BooleanField(default='True'),
        ),
        migrations.AlterField(
            model_name='medic',
            name='status',
            field=models.BooleanField(default='True'),
        ),
    ]
