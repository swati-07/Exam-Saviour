# Generated by Django 2.2 on 2021-01-02 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0016_notes_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'get_latest_by': 'approved'},
        ),
    ]