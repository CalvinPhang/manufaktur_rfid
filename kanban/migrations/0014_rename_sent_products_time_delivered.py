# Generated by Django 4.2 on 2023-05-08 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kanban", "0013_products_time_inspection_unitstorage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="products", old_name="sent", new_name="time_delivered",
        ),
    ]
