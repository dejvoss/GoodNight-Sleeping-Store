# Generated by Django 3.1.2 on 2021-01-25 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gnblog', '0003_remove_post_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postUrl',
            new_name='slug',
        ),
    ]
