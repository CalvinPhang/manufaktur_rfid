# Generated by Django 4.2 on 2023-05-04 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kanban", "0010_order_delivery_date_products_unit_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="kanban.order",
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="rfid",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="sent",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="time_assy1",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="time_assy2",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="time_storage",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="time_warehouse",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
