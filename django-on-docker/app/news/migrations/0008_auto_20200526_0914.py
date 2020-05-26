# Generated by Django 3.0.6 on 2020-05-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200526_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='type',
        ),
        migrations.AddField(
            model_name='news',
            name='published',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
