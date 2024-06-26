# Generated by Django 5.0.4 on 2024-05-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('birth_day', models.DateField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
