# Generated by Django 2.2 on 2020-12-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0015_auto_20201229_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
