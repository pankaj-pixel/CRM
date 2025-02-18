# Generated by Django 5.1.5 on 2025-02-02 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_remove_leads_team'),
        ('teams', '0003_remove_team_created_at_alter_team_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lead', to='teams.team'),
            preserve_default=False,
        ),
    ]
