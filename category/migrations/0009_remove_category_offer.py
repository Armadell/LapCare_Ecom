# Generated by Django 4.1.1 on 2022-10-03 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_rename_offer_status_category_offerstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='offer',
        ),
    ]
