# Generated by Django 4.1.7 on 2023-04-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_application_welder_date_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="welder_date_birth",
            field=models.CharField(
                max_length=150, null=True, verbose_name="Дата рождения сварщика"
            ),
        ),
    ]
