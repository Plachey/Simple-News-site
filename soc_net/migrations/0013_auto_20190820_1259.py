# Generated by Django 2.2.3 on 2019-08-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0012_auto_20190820_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=160),
        ),
    ]
