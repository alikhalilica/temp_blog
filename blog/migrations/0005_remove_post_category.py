# Generated by Django 2.2.11 on 2020-05-09 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
