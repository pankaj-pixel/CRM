# Generated by Django 5.1.5 on 2025-02-02 05:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_alter_team_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='team',
            name='member',
            field=models.ManyToManyField(related_name='team_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
