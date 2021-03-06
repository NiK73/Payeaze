# Generated by Django 3.1.1 on 2020-09-22 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0013_auto_20200920_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dmonth1',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 22, 20, 47, 57, 964357)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth10',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 20, 47, 57, 964587)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth11',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 20, 47, 57, 964610)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth12',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 27, 20, 47, 57, 964638)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth2',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 20, 20, 47, 57, 964392)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth3',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 17, 20, 47, 57, 964422)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth4',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 20, 47, 57, 964447)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth5',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 12, 20, 47, 57, 964471)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth6',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 20, 47, 57, 964494)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth7',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 9, 20, 47, 57, 964518)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth8',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 20, 47, 57, 964541)),
        ),
        migrations.AddField(
            model_name='order',
            name='dmonth9',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 20, 47, 57, 964564)),
        ),
        migrations.AlterField(
            model_name='order',
            name='validity',
            field=models.CharField(default='6', max_length=20),
        ),
    ]
