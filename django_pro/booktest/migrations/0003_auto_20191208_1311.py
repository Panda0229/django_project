# Generated by Django 2.2.5 on 2019-12-08 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20191208_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='btitlt',
            new_name='btitle',
        ),
    ]