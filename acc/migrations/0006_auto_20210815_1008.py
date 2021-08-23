# Generated by Django 3.0.8 on 2021-08-15 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0005_auto_20210815_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='servicename',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='productname',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='servicename',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='name',
            new_name='vendor',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='productname',
        ),
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acc.Customer'),
        ),
    ]