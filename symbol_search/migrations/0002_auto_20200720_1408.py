# Generated by Django 3.0.8 on 2020-07-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symbol_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ipo_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='IPO Year'),
        ),
    ]
