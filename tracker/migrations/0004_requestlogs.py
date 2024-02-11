# Generated by Django 5.0.2 on 2024-02-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_trackinghistory_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_info', models.TextField()),
                ('request_type', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
