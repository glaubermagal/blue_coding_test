# Generated by Django 5.0 on 2023-12-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
