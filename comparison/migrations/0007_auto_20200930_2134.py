# Generated by Django 3.1.1 on 2020-09-30 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0006_auto_20200930_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filtervalue',
            old_name='fimal_values',
            new_name='final_values',
        ),
    ]
