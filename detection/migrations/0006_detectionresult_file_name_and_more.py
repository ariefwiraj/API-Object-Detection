# Generated by Django 4.2.13 on 2024-08-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("detection", "0005_detectionresult_image_base64"),
    ]

    operations = [
        migrations.AddField(
            model_name="detectionresult",
            name="file_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="detectionresult",
            name="id_predictions",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="detectionresult",
            name="image_base64",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="detectionresult",
            name="mask_data",
            field=models.JSONField(),
        ),
    ]
