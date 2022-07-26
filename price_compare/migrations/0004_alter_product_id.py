# Generated by Django 4.0.6 on 2022-07-26 15:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('price_compare', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('78a5b1de-408c-4995-92d8-4a762c656f52'), primary_key=True, serialize=False, unique=True),
        ),
    ]
