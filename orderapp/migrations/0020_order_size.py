# Generated by Django 4.2.6 on 2023-12-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0019_remove_order_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
