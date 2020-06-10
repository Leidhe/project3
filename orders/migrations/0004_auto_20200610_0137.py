# Generated by Django 3.0.7 on 2020-06-10 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200608_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price_small', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_large', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='orders.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_dishes',
        ),
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='orderdish',
            name='additions',
        ),
        migrations.RemoveField(
            model_name='orderdish',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='orderdish',
            name='toppings',
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Topping'),
        ),
        migrations.DeleteModel(
            name='Addition',
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDish',
        ),
    ]