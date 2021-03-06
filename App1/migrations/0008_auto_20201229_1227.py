# Generated by Django 2.2 on 2020-12-29 06:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0007_auto_20201229_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='name',
        ),
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='App1.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notes',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 29, 6, 56, 57, 16019, tzinfo=utc)),
        ),
    ]
