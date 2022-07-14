# Generated by Django 4.0.6 on 2022-07-14 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_note_note_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(choices=[('Top note', 'Top note'), ('Middle note', 'Middle note'), ('Base note', 'Base note')], default='Top note', max_length=15),
        ),
    ]
