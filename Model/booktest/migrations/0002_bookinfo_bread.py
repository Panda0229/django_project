# Generated by Django 2.2.5 on 2019-12-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='bread',
            field=models.IntegerField(default=0),
        ),
    ]
