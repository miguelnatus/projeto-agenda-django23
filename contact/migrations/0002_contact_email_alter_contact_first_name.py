# Generated by Django 4.2.1 on 2023-05-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
