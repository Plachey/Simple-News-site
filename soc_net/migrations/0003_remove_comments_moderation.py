# Generated by Django 2.2.4 on 2019-08-18 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0002_auto_20190817_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='moderation',
        ),
    ]