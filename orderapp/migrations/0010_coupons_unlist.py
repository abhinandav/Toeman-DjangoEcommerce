# Generated by Django 4.2.6 on 2023-11-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0009_coupons_usercoupons'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='unlist',
            field=models.BooleanField(default=False),
        ),
    ]