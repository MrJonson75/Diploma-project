# Generated by Django 5.1.1 on 2024-10-07 19:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_gamepost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamepost',
            name='excerpt',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Краткое содержание статьи', verbose_name='Кратко'),
        ),
        migrations.AlterField(
            model_name='newsblock',
            name='excerpt',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Краткое содержание новости, заполнять не обязательно.', verbose_name='Кратко'),
        ),
    ]
