# Generated by Django 3.1.7 on 2021-04-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210421_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customershippingaddress',
            name='note',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
