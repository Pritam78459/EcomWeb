# Generated by Django 3.1.6 on 2021-02-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='defaultpic.jpg', upload_to='product_pics'),
        ),
    ]