# Generated by Django 3.0.1 on 2020-01-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_auto_20200128_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendvisitor',
            name='response',
            field=models.CharField(blank=True, choices=[('not collected', 'not collected'), ('collected', 'collected')], default='not collected', max_length=50),
        ),
        migrations.AlterField(
            model_name='friendvisitor',
            name='status',
            field=models.CharField(blank=True, choices=[('allow', 'Allow'), ('pending', 'Pending')], default='pending', max_length=50),
        ),
    ]
