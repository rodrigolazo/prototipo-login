# Generated by Django 3.0.8 on 2020-07-21 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
