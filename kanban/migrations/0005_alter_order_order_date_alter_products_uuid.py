# Generated by Django 4.2 on 2023-04-20 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kanban", "0004_remove_order_delivery_date_remove_order_product_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="uuid",
            field=models.UUIDField(default="ef7937cb35b240cda61ef98a144a8a2a"),
        ),
    ]
