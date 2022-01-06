# Generated by Django 3.2.10 on 2022-01-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_companies_startups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitments',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('indystry', models.CharField(max_length=32)),
                ('response_rate', models.FloatField()),
                ('response_day', models.IntegerField()),
                ('logo', models.CharField(max_length=256)),
                ('update_date', models.DateField()),
            ],
        ),
    ]