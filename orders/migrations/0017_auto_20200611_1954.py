# Generated by Django 3.0.7 on 2020-06-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20200611_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='subs_extra',
            field=models.ManyToManyField(blank='True', related_name='orderitem_subsextras', to='orders.Sub_Extra'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='toppings',
            field=models.ManyToManyField(blank='True', related_name='orderitem_toppings', to='orders.Topping'),
        ),
    ]