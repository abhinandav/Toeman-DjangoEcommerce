# Generated by Django 4.2.6 on 2023-12-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_alter_productattribute_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='size',
            field=models.PositiveIntegerField(choices=[(6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]