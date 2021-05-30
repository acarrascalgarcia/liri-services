# Generated by Django 3.2.3 on 2021-05-30 01:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid'),
        ),
    ]