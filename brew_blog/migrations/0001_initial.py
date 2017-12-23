# Generated by Django 2.0 on 2017-12-16 16:45

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('date', models.DateField(blank=True, null=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
    ]