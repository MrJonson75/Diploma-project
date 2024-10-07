# Generated by Django 5.1.1 on 2024-10-02 21:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_gamepost_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(auto_created=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'), max_length=254, verbose_name='e-mail')),
                ('content', models.TextField(blank=True, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Время редактирования')),
                ('active', models.BooleanField(default=True, verbose_name='Статус')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='blog.gamepost', verbose_name='Статья')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
