# Generated by Django 2.1.3 on 2018-11-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20181031_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='universidad',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
