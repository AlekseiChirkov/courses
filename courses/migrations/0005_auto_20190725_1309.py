# Generated by Django 2.2.3 on 2019-07-25 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190725_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='course',
        ),
    ]
