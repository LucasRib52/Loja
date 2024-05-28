# Generated by Django 5.0.4 on 2024-05-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stores_count', models.IntegerField()),
                ('stores_value', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]