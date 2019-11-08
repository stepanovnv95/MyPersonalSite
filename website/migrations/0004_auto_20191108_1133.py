# Generated by Django 2.2.5 on 2019-11-08 07:33

from django.db import migrations, models
import django.utils.timezone
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20191027_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='media_directory',
            field=models.CharField(default=website.models.generate_media_directory_name, editable=False, max_length=35),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]