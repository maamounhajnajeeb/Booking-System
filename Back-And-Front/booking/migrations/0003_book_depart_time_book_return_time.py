# Generated by Django 4.0.10 on 2023-08-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_book_depart_time_remove_book_return_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='depart_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='return_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
