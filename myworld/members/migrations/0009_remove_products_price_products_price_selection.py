# Generated by Django 4.1 on 2022-09-02 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_runner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Price',
        ),
        migrations.AddField(
            model_name='products',
            name='Price_Selection',
            field=models.CharField(blank=True, choices=[('100', '100'), ('50', '50'), ('20', '20')], max_length=10),
        ),
    ]
