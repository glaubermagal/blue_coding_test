# Generated by Django 5.0 on 2023-12-21 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0002_remove_urls_redirect_to_alter_urls_base62_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]