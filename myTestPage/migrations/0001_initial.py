# Generated by Django 4.1.3 on 2022-12-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="myTestPageDB",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=10)),
                ("age", models.IntegerField()),
            ],
        ),
    ]
