# Generated by Django 5.0.2 on 2024-03-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0002_remove_producer_aadharnumber_remove_producer_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='address',
            field=models.CharField(max_length=110, null=True),
        ),
    ]
