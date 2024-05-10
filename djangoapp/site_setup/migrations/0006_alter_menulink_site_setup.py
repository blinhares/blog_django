# Generated by Django 5.0.6 on 2024-05-10 19:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0005_alter_sitesetup_description_alter_sitesetup_favicon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulink',
            name='site_setup',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='site_setup.sitesetup'),
        ),
    ]
