# Generated by Django 3.0.1 on 2020-01-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200109_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanupload',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=50),
        ),
    ]
