# Generated by Django 5.1.1 on 2024-09-29 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
