# Generated by Django 3.0.5 on 2020-06-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_specialupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
            ],
        ),
    ]
