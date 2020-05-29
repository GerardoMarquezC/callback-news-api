# Generated by Django 3.0.6 on 2020-05-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time when object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time when object last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=150, verbose_name='category name')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]