# Generated by Django 3.0.5 on 2020-06-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200626_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dwedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('package', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=300)),
                ('contact', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
