# Generated by Django 3.2.13 on 2022-06-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default=None)),
                ('avatar', models.ImageField(default=None, upload_to='uploads/directors/%Y/%m')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
