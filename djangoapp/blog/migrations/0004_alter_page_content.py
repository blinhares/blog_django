# Generated by Django 5.0.6 on 2024-05-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_page_content_page_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(),
        ),
    ]
