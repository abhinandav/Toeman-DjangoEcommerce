# Generated by Django 4.2.6 on 2023-12-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0028_alter_productattribute_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='size',
            field=models.PositiveIntegerField(),
        ),
    ]