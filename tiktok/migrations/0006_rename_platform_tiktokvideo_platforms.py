# Generated by Django 4.1.5 on 2023-01-22 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiktok', '0005_tiktokvideo_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiktokvideo',
            old_name='platform',
            new_name='platforms',
        ),
    ]
