# Generated by Django 2.2.4 on 2019-09-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0023_auto_20190903_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='moderation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateField(),
        ),
    ]
