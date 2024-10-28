# Generated by Django 5.1.2 on 2024-10-27 18:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capitalminded', '0006_loanpayment_due_date_loanpayment_interest_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessregistration',
            name='available_shares',
            field=models.IntegerField(blank=True, default=1000000, null=True),
        ),
        migrations.AddField(
            model_name='businessregistration',
            name='share_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=10.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='businessregistration',
            name='total_shares',
            field=models.IntegerField(blank=True, default=1000000, null=True),
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shares', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capitalminded.businessregistration')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
