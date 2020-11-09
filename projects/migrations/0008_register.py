# Generated by Django 3.0.5 on 2020-07-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
