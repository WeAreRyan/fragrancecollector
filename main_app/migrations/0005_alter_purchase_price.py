# Generated by Django 4.0.6 on 2022-07-13 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_purchase_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
