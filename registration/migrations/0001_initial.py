# Generated by Django 4.1.7 on 2023-02-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=50)),
                ('s_email', models.EmailField(max_length=254)),
                ('s_password', models.CharField(max_length=100)),
                ('s_profile', models.ImageField(upload_to='student/')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=50)),
                ('t_email', models.EmailField(max_length=254)),
                ('t_password', models.CharField(max_length=100)),
                ('t_profile', models.ImageField(upload_to='teacher/')),
            ],
        ),
    ]
