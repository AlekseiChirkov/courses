# Generated by Django 2.2.2 on 2019-06-28 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactvalue',
            old_name='value',
            new_name='name',
        ),
    ]