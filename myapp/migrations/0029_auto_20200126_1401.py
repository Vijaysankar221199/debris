# Generated by Django 3.0.1 on 2020-01-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20200126_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendvisitor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='friendvisitor',
            name='name',
        ),
        migrations.AddField(
            model_name='friendvisitor',
            name='Location',
            field=models.CharField(blank=True, choices=[('Area A', 'Area A'), ('Area B', 'Area B'), ('Area C', 'Area C')], max_length=50, null=True),
        ),
    ]
