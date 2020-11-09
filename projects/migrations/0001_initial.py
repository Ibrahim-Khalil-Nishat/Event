# Generated by Django 3.0.5 on 2020-06-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corporate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('booking_details', models.TextField()),
                ('date', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
