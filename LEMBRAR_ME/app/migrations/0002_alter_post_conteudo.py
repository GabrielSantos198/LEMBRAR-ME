# Generated by Django 3.2.6 on 2021-08-17 11:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
