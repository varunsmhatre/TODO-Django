# Generated by Django 4.1.7 on 2023-03-12 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="start_date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
