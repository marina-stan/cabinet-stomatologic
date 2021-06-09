# Generated by Django 2.2.24 on 2021-06-07 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementcabinet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('id_no', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('specialization', models.CharField(max_length=200)),
                ('graduation_date', models.DateTimeField()),
                ('notes', models.CharField(max_length=1200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='medic',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='medic',
            name='email',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='medic',
            name='graduation_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='medic',
            name='id_no',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='medic',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='medic',
            name='specialization',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='medic',
            name='status',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='medic',
            name='university',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
