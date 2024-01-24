# Generated by Django 5.0 on 2024-01-24 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_facility", "0012_alter_holiday_unique_together_and_more"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthfacility",
            name="site",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.site",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealthfacility",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.site",
            ),
        ),
    ]
