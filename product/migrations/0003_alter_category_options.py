# Generated by Django 4.1 on 2022-08-19 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_product_input_value"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
