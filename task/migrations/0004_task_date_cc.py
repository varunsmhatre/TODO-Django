# Generated by Django 4.1.7 on 2023-03-15 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0003_remove_task_desc"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date_cc",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
