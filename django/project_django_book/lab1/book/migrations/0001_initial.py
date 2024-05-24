# Generated by Django 5.0.4 on 2024-04-22 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('version', models.IntegerField(default=1)),
                ('latest_version_date', models.DateTimeField(auto_now=True)),
                ('image', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
