# Generated by Django 2.2 on 2020-12-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='notes',
            field=models.FileField(upload_to=''),
        ),
    ]