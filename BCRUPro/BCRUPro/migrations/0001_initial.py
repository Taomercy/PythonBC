# Generated by Django 3.0 on 2020-11-09 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteBids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation_id', models.TextField(unique=True)),
                ('network_type', models.TextField()),
                ('area', models.TextField()),
                ('time', models.TextField()),
                ('number', models.TextField()),
                ('data', models.TextField()),
                ('sign_status', models.CharField(choices=[('signed', 'signed'), ('unsigned', 'unsigned')], default='unsigned', max_length=32)),
                ('process_status', models.CharField(choices=[('opening', 'opening'), ('closed', 'closed')], default='opening', max_length=32)),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubmitBids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.TextField(unique=True)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('signed', 'signed'), ('unsigned', 'unsigned')], default='unsigned', max_length=32)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('invite_bid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BCRUPro.InviteBids')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.User')),
            ],
        ),
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
        migrations.AddField(
            model_name='invitebids',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BCRUPro.Node'),
        ),
        migrations.AddField(
            model_name='invitebids',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.User'),
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
