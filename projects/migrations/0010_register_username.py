# Generated by Django 3.0.5 on 2020-07-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_register_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
