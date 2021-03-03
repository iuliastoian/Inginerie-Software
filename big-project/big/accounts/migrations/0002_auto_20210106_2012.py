# Generated by Django 3.1.4 on 2021-01-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_doctor',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='is_nurse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nurse',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nurse',
            name='is_nurse',
            field=models.BooleanField(default=True),
        ),
    ]
