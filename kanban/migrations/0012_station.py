# Generated by Django 4.2 on 2023-05-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kanban", "0011_alter_products_order_alter_products_rfid_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Station",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "instruction",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
    ]
