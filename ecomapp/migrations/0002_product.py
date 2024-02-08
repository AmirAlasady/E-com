# Generated by Django 4.2.4 on 2023-12-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('catagory', models.CharField(default='', max_length=50)),
                ('subcatagory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='shop/images')),
            ],
        ),
    ]
