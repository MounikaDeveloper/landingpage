# Generated by Django 3.1.1 on 2020-10-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201006_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingformmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
