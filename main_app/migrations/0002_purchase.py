# Generated by Django 4.0.6 on 2022-07-13 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='purchase date')),
                ('size', models.CharField(choices=[(30, '1 FL. OZ. or 30 mL'), (50, '1.7 FL. OZ or 50 mL'), (75, '2.5 FL. OZ. or 75 mL'), (100, '3.4 FL. OZ. or 100 mL'), (125, '4.2 FL. OZ or 125 mL')], default=30, max_length=3)),
                ('fragrance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.fragrance')),
            ],
        ),
    ]
