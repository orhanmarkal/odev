# Generated by Django 3.1.5 on 2021-01-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_delete_poststatistic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read',
            field=models.IntegerField(default=0),
        ),
    ]
