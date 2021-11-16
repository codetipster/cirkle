# Generated by Django 3.2.9 on 2021-11-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Full name', max_length=40)),
                ('phone_number', models.IntegerField(unique=True)),
                ('email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('relation', models.CharField(choices=[('Friend', 'a friend'), ('Family', 'met as family'), ('Office', 'met at the office'), ('Stranger', 'A stranger')], max_length=50)),
            ],
        ),
    ]
