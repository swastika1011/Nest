# Generated by Django 5.1.1 on 2024-10-02 22:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("owasp", "0006_alter_chapter_currency_alter_chapter_level_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chapter",
            name="suggested_location",
            field=models.CharField(
                blank=True, default="", max_length=100, verbose_name="Suggested location"
            ),
        ),
    ]
