# Generated by Django 4.2.14 on 2024-10-20 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_customer_email_alter_customer_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Visit',
        ),
    ]
