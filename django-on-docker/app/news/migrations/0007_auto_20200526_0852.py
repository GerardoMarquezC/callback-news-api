# Generated by Django 3.0.6 on 2020-05-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_media_url'),
        ('news', '0006_auto_20200526_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='media',
        ),
        migrations.AddField(
            model_name='news',
            name='media',
            field=models.ManyToManyField(null=True, related_name='news_media', to='media.Media'),
        ),
    ]
