# Generated by Django 4.1.1 on 2022-10-03 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_rename_is_discount_active_products_offer_statuspro_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='offer_statuspro',
            new_name='offerstatuspro',
        ),
    ]
