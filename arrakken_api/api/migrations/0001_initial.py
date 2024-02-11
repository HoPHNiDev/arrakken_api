# Generated by Django 5.0.2 on 2024-02-11 08:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='api_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_user_id', models.CharField(max_length=20, unique=True, verbose_name='Telegram ID')),
                ('for_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='for_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
