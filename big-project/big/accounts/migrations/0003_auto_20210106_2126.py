# Generated by Django 3.1.4 on 2021-01-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210106_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='email',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
