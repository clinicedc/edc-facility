# Generated by Django 2.2.3 on 2019-09-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_facility", "0002_auto_20180102_1158")]

    operations = [
        migrations.AlterField(
            model_name="holiday", name="country", field=models.CharField(max_length=50)
        ),
        migrations.AlterField(
            model_name="holiday", name="name", field=models.CharField(max_length=50)
        ),
    ]
