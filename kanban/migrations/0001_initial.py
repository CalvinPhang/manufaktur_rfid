# Generated by Django 4.2 on 2023-04-20 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("uuid", models.UUIDField(default="4d99fdf560b9488fbd1382cc3e582567")),
                ("quantity", models.IntegerField()),
                ("supplier", models.CharField(max_length=255)),
                ("requested_by", models.CharField(max_length=255)),
                ("order_date", models.DateField()),
                ("delivery_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="PartType",
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="UnitType",
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="UnitPartsBom",
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
                ("part_quantity", models.IntegerField()),
                (
                    "part_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="part_type",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="kanban.parttype",
                        to_field="name",
                    ),
                ),
                (
                    "unit_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="unit_type",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="kanban.unittype",
                        to_field="name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Products",
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
                ("uuid", models.UUIDField(default="4d3a8afffac6402f9c12a60c95067bf5")),
                (
                    "order_id",
                    models.ForeignKey(
                        blank=True,
                        db_column="order_id",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="kanban.order",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PartsInventory",
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
                ("quantity", models.IntegerField()),
                (
                    "part_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="part_type",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="kanban.parttype",
                        to_field="name",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="product_id",
            field=models.ForeignKey(
                blank=True,
                db_column="unit_type",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="kanban.unittype",
                to_field="name",
            ),
        ),
        migrations.CreateModel(
            name="Inventory",
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
                ("quantity", models.IntegerField()),
                (
                    "unit_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="unit_type",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="kanban.unittype",
                        to_field="name",
                    ),
                ),
            ],
        ),
    ]
