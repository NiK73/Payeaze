# Generated by Django 3.1 on 2020-09-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0007_auto_20200908_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]