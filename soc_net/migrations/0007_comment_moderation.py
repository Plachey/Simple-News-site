# Generated by Django 2.2.4 on 2019-08-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0006_auto_20190818_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='moderation',
            field=models.BooleanField(default=False),
        ),
    ]