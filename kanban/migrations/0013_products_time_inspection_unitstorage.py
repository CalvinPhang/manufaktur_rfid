# Generated by Django 4.2 on 2023-05-04 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kanban", "0012_station"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="time_inspection",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="UnitStorage",
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
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kanban.unittype",
                    ),
                ),
            ],
        ),
    ]
