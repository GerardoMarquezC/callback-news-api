# Generated by Django 3.0.6 on 2020-05-26 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20200526_0528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='users',
            new_name='user',
        ),
    ]
