# Generated by Django 2.2.11 on 2020-05-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Category'),
        ),
    ]
