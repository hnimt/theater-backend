# Generated by Django 3.2.13 on 2022-06-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
