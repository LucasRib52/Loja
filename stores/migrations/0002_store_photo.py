# Generated by Django 5.0.4 on 2024-04-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='stores/'),
        ),
    ]