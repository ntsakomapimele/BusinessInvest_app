# Generated by Django 5.1.2 on 2024-10-26 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=255)),
                ('ownership', models.CharField(max_length=255)),
                ('tax_reg', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('annual_revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_info', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('business_plan', models.FileField(blank=True, null=True, upload_to='business_plans/')),
                ('financial_statements', models.FileField(blank=True, null=True, upload_to='financial_statements/')),
                ('legal_documents', models.FileField(blank=True, null=True, upload_to='legal_documents/')),
                ('management_profiles', models.FileField(blank=True, null=True, upload_to='management_profiles/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BusinessResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='capitalminded.businesstype')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MicroLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_requested', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('term_months', models.IntegerField()),
                ('purpose', models.TextField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('ACTIVE', 'Active'), ('PAID', 'Paid')], default='PENDING', max_length=20)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('monthly_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('next_payment_date', models.DateField()),
                ('total_payments_made', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('remaining_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_frequency', models.CharField(choices=[('MONTHLY', 'Monthly'), ('BI_WEEKLY', 'Bi-Weekly'), ('WEEKLY', 'Weekly')], default='MONTHLY', max_length=20)),
                ('performance_score', models.IntegerField(default=100)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capitalminded.businessregistration')),
            ],
        ),
    ]
