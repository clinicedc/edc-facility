# Generated by Django 4.2.3 on 2023-07-25 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("edc_facility", "0005_healthfacility_healthfacilitytypes_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthfacility",
            name="health_facility_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_facility.healthfacilitytypes",
                verbose_name="Health facility type",
            ),
        ),
    ]
