# Generated by Django 3.0.2 on 2020-01-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]