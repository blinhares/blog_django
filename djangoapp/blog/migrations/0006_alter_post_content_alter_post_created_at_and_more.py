# Generated by Django 5.0.6 on 2024-05-10 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Conteudo do Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Data da criação. Automatico.'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(help_text='Um breve resumo do Post.', max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Data da Modificação. Automatico.'),
        ),
    ]
