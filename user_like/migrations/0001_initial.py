# Generated by Django 3.2.6 on 2022-03-08 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_like',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_like', models.CharField(max_length=100)),
            ],
        ),
    ]
