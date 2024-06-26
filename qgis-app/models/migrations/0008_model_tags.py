# Generated by Django 4.2.13 on 2024-06-12 06:04

from django.db import migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('models', '0007_alter_review_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
