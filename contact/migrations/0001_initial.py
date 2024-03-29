# Generated by Django 4.2.1 on 2023-05-18 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('first_name', models.EmailField(blank=True, max_length=50)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
