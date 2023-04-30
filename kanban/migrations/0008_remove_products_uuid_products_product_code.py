# Generated by Django 4.2 on 2023-04-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kanban", "0007_remove_products_order_id_products_order_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="products", name="uuid",),
        migrations.AddField(
            model_name="products",
            name="product_code",
            field=models.CharField(default="TEST", max_length=200),
            preserve_default=False,
        ),
    ]
