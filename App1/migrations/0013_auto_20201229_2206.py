# Generated by Django 2.2 on 2020-12-29 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0012_notes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.Profile'),
        ),
    ]
