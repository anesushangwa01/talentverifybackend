# Generated by Django 5.1.8 on 2025-04-03 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('register_number', models.CharField(max_length=100, unique=True)),
                ('register_date', models.DateField()),
                ('company_address', models.TextField()),
                ('contact_person', models.CharField(max_length=255)),
                ('number_of_employees', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('departments', models.TextField(help_text='Comma separated list of departments')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_id', models.CharField(max_length=50, unique=True)),
                ('current_role', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('left_date', models.DateField(blank=True, null=True)),
                ('duties', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='talentverify.company')),
            ],
        ),
    ]
