<<<<<<< HEAD
# Generated by Django 3.2.3 on 2021-05-30 18:14
=======
# Generated by Django 3.2.3 on 2021-05-30 01:06
>>>>>>> 4b6ed126233285efef0f86abd3ff9e8b1ab2988f

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
<<<<<<< HEAD
import uuid
=======
>>>>>>> 4b6ed126233285efef0f86abd3ff9e8b1ab2988f


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, default='', max_length=30, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=60, verbose_name='last name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
=======
                ('uuid', models.UUIDField(unique=True, verbose_name='uuid')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=60, verbose_name='last name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
>>>>>>> 4b6ed126233285efef0f86abd3ff9e8b1ab2988f
        ),
    ]
