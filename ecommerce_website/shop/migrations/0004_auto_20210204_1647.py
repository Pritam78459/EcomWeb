# Generated by Django 3.1.6 on 2021-02-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210204_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='product_pics'),
        ),
    ]