# Generated by Django 3.0.7 on 2020-06-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200608_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='num_toppings',
            field=models.IntegerField(default=0),
        ),
    ]
