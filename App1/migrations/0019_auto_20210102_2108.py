# Generated by Django 2.2 on 2021-01-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0018_auto_20210102_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='institute',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]