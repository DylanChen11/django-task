# Generated by Django 3.2 on 2023-03-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('age', models.IntegerField()),
                ('uid', models.IntegerField(unique=True)),
            ],
        ),
    ]
