# Generated by Django 4.2 on 2023-04-20 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kanban", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="product_id",
            field=models.ForeignKey(
                blank=True,
                db_column="product_id",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="kanban.unittype",
                to_field="name",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="uuid",
            field=models.UUIDField(default="7780f64f0c7f4c4b99d01118827f45d8"),
        ),
        migrations.AlterField(
            model_name="products",
            name="uuid",
            field=models.UUIDField(default="83bf03d9679b413f9d85bd02b54652ea"),
        ),
    ]
