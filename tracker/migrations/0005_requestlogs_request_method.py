# Generated by Django 5.0.2 on 2024-02-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_requestlogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlogs',
            name='request_method',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]