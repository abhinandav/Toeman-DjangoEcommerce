# Generated by Django 4.2.6 on 2023-12-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_productattribute_unlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='size',
            field=models.PositiveIntegerField(choices=[(6, 'Size 6'), (7, 'Size 7'), (8, 'Size 8'), (9, 'Size 9'), (10, 'Size 10')]),
        ),
    ]