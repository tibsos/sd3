# Generated by Django 4.2.14 on 2024-10-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_customer_email_alter_customer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='website_type',
            field=models.TextField(null=True),
        ),
    ]
