# Generated by Django 3.0.2 on 2020-01-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20200118_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='emg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
    ]
