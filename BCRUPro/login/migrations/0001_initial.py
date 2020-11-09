# Generated by Django 3.0 on 2020-11-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('customer', 'customer'), ('csp', 'csp')], default='customer', max_length=32)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['c_time'],
            },
        ),
    ]
