# Generated by Django 2.2.4 on 2019-08-29 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0019_auto_20190829_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
    ]
