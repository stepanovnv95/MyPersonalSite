# Generated by Django 2.2.5 on 2019-10-27 06:53

from django.db import migrations, models
# import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='preview_image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='publish_date',
            # field=models.DateTimeField(default=website.models.get_default_datetime),
            field=models.DateTimeField(),
        ),
    ]
