# Generated by Django 4.1.5 on 2023-07-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webtranfer', '0003_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=50)),
                ('field2', models.CharField(max_length=50)),
            ],
        ),
    ]
