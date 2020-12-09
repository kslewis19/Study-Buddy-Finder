# Generated by Django 3.1.1 on 2020-11-12 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddyfinder', '0023_merge_20201110_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon', models.BooleanField(default=False)),
                ('tues', models.BooleanField(default=False)),
                ('wed', models.BooleanField(default=False)),
                ('thurs', models.BooleanField(default=False)),
                ('fri', models.BooleanField(default=False)),
                ('sat', models.BooleanField(default=False)),
                ('sun', models.BooleanField(default=False)),
                ('scheduler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduler', to='studybuddyfinder.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='calendars',
            field=models.ManyToManyField(blank=True, to='studybuddyfinder.Calendar'),
        ),
    ]
