# Generated by Django 2.2 on 2019-04-23 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0002_auto_20190423_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
