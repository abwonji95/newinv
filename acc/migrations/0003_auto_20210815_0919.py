# Generated by Django 3.0.8 on 2021-08-15 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_auto_20210815_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchases',
            old_name='productname',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='product_description',
            new_name='service_description',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='items',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='items',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='status',
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='price',
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchases',
            name='quantity',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
