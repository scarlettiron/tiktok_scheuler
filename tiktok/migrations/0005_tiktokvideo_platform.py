# Generated by Django 4.1.5 on 2023-01-22 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialPlatforms', '0002_social_active'),
        ('tiktok', '0004_tiktokvideo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiktokvideo',
            name='platform',
            field=models.ManyToManyField(to='SocialPlatforms.social'),
        ),
    ]
