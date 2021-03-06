# Generated by Django 3.2.13 on 2022-06-11 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seat', '0001_initial'),
        ('invoice', '0001_initial'),
        ('schedule_movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleSeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_booked', models.BooleanField(default=False)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule_seats', to='invoice.invoice')),
                ('schedule_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_seats', to='schedule_movie.schedulemovie')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_seats', to='seat.seat')),
            ],
            options={
                'db_table': 'theater_schedule_seat',
                'unique_together': {('schedule_movie', 'seat')},
            },
        ),
    ]
