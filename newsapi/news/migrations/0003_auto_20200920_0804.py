# Generated by Django 3.0.7 on 2020-09-20 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200920_0555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='publication_data',
            new_name='publication_date',
        ),
    ]
