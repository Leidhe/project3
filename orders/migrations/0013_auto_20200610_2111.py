# Generated by Django 3.0.7 on 2020-06-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200610_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem1',
            name='price_small',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]