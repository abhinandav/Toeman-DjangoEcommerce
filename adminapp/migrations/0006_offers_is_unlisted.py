# Generated by Django 4.2.6 on 2023-11-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_alter_offers_category_alter_offers_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='is_unlisted',
            field=models.BooleanField(default=False),
        ),
    ]