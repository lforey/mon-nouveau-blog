# Generated by Django 2.2.28 on 2023-11-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='lieu',
            new_name='activity',
        ),
        migrations.AddField(
            model_name='player',
            name='etat',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
