# Generated by Django 2.1.7 on 2019-03-16 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20190316_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='date_time',
        ),
    ]