# Generated by Django 4.2.14 on 2024-10-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_buttonclick'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.TextField(default='s'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='website_type',
            field=models.TextField(default='s'),
            preserve_default=False,
        ),
    ]
