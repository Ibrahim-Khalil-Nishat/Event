# Generated by Django 3.0.5 on 2020-06-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dcorporate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Details', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Corporate',
        ),
    ]
