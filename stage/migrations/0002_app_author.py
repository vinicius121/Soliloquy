# Generated by Django 2.2.4 on 2019-08-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='author',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
