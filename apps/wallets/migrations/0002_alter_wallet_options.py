# Generated by Django 3.2.3 on 2021-06-22 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wallet',
            options={'verbose_name': 'wallet', 'verbose_name_plural': 'wallets'},
        ),
    ]
