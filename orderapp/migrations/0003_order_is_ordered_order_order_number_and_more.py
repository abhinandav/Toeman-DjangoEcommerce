# Generated by Django 4.2.6 on 2023-11-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_remove_order_ip_remove_order_is_ordered_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned')], default='New', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]