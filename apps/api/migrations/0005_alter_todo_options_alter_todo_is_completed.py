# Generated by Django 5.0.4 on 2024-04-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_user_options_user_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Cписок дел', 'verbose_name_plural': 'Cписки дел'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Выполнен'),
        ),
    ]
