# Generated by Django 3.1.1 on 2020-10-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddyfinder', '0007_auto_20201022_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hide_state',
            field=models.BooleanField(default=False),
        ),
    ]
