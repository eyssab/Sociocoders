# Generated by Django 5.0.4 on 2024-04-30 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0002_customuser_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_name',
            field=models.CharField(default='', max_length=15),
        ),
    ]
