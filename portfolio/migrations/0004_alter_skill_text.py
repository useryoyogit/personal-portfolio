# Generated by Django 3.2.7 on 2022-03-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='text',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
