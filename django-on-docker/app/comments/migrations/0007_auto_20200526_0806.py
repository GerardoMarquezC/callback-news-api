# Generated by Django 3.0.6 on 2020-05-26 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200526_0528'),
        ('comments', '0006_auto_20200526_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='news.News'),
        ),
    ]