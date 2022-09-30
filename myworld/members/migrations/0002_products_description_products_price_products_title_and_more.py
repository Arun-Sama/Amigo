# Generated by Django 4.1 on 2022-09-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Description',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='products',
            name='Price',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='products',
            name='Title',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='products',
            name='Summary',
            field=models.TextField(default='This is so cool!', max_length=300),
        ),
    ]