# Generated by Django 3.2.6 on 2021-08-10 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
