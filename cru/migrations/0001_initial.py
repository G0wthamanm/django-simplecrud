# Generated by Django 2.2.19 on 2022-04-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=15)),
                ('last', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]