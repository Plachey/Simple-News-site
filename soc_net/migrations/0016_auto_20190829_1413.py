# Generated by Django 2.2.4 on 2019-08-29 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0015_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='users_reaction',
        ),
    ]