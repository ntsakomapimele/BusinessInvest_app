# Generated by Django 5.1.2 on 2024-10-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capitalminded', '0007_businessregistration_available_shares_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessregistration',
            name='available_shares',
            field=models.IntegerField(default=1000000),
        ),
        migrations.AlterField(
            model_name='businessregistration',
            name='share_price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='businessregistration',
            name='total_shares',
            field=models.IntegerField(default=1000000),
        ),
    ]