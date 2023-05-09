# Generated by Django 4.1.7 on 2023-05-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=24)),
                ('place', models.CharField(max_length=255)),
                ('member_limit', models.IntegerField(max_length=50)),
                ('date', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]