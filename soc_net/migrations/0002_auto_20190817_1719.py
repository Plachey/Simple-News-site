# Generated by Django 2.2.4 on 2019-08-17 14:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 8, 17, 14, 19, 13, 794279, tzinfo=utc), verbose_name='Date add'),
            preserve_default=False,
        ),
    ]
