# Generated by Django 5.0.4 on 2024-04-24 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_user_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
