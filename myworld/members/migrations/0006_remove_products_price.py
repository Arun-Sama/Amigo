# Generated by Django 4.1 on 2022-09-02 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_shirt_alter_cart_product_delete_album_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Price',
        ),
    ]
