# Generated by Django 3.2.6 on 2022-03-08 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=100)),
            ],
        ),
    ]
