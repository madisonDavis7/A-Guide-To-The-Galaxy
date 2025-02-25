# Generated by Django 5.1.2 on 2024-11-17 23:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_spacetravelerprofile_regular_account_and_more'),
        ('socialaccount', '0006_alter_socialaccount_extra_data'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='spacetravelerprofile',
            name='regular_account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='spacetravelerprofile',
            name='social_account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profile', to='socialaccount.socialaccount'),
        ),
    ]
