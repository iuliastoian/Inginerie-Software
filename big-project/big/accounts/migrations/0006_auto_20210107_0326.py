# Generated by Django 3.1.4 on 2021-01-07 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210107_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
    ]
