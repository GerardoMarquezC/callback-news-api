# Generated by Django 3.0.6 on 2020-05-30 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20200527_0528'),
        ('media', '0006_media_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='news_related',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media_news', to='news.News'),
        ),
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='media',
            name='type',
            field=models.CharField(choices=[('image', 'image'), ('video', 'video'), ('audio', 'audio'), ('slides', 'slides'), ('other', 'other')], default='image', max_length=50),
        ),
        migrations.AlterField(
            model_name='media',
            name='url',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]
