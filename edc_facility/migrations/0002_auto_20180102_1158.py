# Generated by Django 2.0 on 2018-01-02 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("edc_facility", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="holiday", options={"ordering": ["country", "local_date"]}
        ),
        migrations.AddField(
            model_name="holiday",
            name="country",
            field=models.CharField(default="botswana", max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="holiday",
            name="local_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="holiday",
            name="name",
            field=models.CharField(default="holiday", max_length=25),
            preserve_default=False,
        ),
        migrations.RemoveField(model_name="holiday", name="day"),
        migrations.AlterUniqueTogether(
            name="holiday", unique_together={("country", "local_date")}
        ),
    ]
