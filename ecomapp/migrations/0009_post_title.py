# Generated by Django 4.2.4 on 2023-12-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0008_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]