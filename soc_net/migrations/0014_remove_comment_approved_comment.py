# Generated by Django 2.2.3 on 2019-08-20 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0013_auto_20190820_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]