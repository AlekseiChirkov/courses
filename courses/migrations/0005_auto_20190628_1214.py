# Generated by Django 2.2.2 on 2019-06-28 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_contactvalue_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('PHONE', 'PHONE'), ('FACEBOOK', 'FACEBOOK'), ('EMAIL', 'EMAIL')], default='', max_length=64),
        ),
    ]