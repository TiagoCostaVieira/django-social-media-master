# Generated by Django 3.2.7 on 2021-09-26 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="password",
            field=models.CharField(max_length=255),
        ),
    ]