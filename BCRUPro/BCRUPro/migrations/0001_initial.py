# Generated by Django 3.0.7 on 2020-08-19 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.TextField(unique=True)),
                ('location', models.TextField()),
                ('today_revenue', models.BigIntegerField(default=0)),
                ('summary_revenue', models.BigIntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True)),
                ('block_id', models.TextField(unique=True)),
                ('previous_hash', models.TextField(default='1')),
                ('proof', models.IntegerField(default=0)),
                ('revenue', models.IntegerField(default=0)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BCRUPro.Node')),
            ],
        ),
    ]
