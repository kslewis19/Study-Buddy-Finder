# Generated by Django 3.1.1 on 2020-09-30 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddyfinder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='qty',
            new_name='year',
        ),
    ]