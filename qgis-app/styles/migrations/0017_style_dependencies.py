# Generated by Django 4.2.16 on 2024-09-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0016_style_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='dependencies',
            field=models.TextField(blank=True, help_text='Comma-separated list for the plugin the resource needs', null=True, verbose_name='Plugin dependencies'),
        ),
    ]
