# Generated by Django 5.1.1 on 2024-10-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_tagarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamepost',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='blog.tagarticle'),
        ),
    ]
