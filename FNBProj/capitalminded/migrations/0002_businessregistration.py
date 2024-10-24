# Generated by Django 5.0.7 on 2024-10-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("capitalminded", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BusinessRegistration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("business_name", models.CharField(max_length=255)),
                ("ownership", models.TextField()),
                ("tax_reg", models.CharField(max_length=100)),
                ("industry", models.CharField(max_length=100)),
                (
                    "annual_revenue",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("product_info", models.TextField()),
                ("business_plan", models.FileField(upload_to="business_plans/")),
                (
                    "financial_statements",
                    models.FileField(upload_to="financial_statements/"),
                ),
                ("legal_documents", models.FileField(upload_to="legal_documents/")),
                (
                    "management_profiles",
                    models.FileField(upload_to="management_profiles/"),
                ),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
