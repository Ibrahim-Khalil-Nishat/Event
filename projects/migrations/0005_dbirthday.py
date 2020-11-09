# Generated by Django 3.0.5 on 2020-06-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_dwedding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dbirthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Details', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=300)),
                ('contact', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]