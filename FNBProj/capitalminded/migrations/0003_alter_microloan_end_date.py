# Generated by Django 5.1.2 on 2024-10-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capitalminded', '0002_loanpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microloan',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
