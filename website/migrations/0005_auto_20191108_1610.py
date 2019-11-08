# Generated by Django 2.2.5 on 2019-11-08 12:10

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20191108_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to=website.models.get_preview_image_upload_path),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]