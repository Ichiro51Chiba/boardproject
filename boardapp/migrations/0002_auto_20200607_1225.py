# Generated by Django 3.0.6 on 2020-06-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodels',
            name='good',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodels',
            name='read',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodels',
            name='readtext',
            field=models.CharField(blank=True, default='a', max_length=100, null=True),
        ),
    ]
