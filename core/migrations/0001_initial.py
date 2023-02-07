# Generated by Django 4.1.4 on 2023-02-07 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='A brief, optional description of this Arc')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arcs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.arc')),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Parameter name')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Brief, optional description of Parameter')),
                ('level', models.IntegerField(default=10, verbose_name='Experience level of this Parameter')),
                ('xp', models.IntegerField(default=0, verbose_name='Experience points gained for this Parameter since last level up')),
                ('total_xp', models.IntegerField(default=0, verbose_name='Total experience points gained for this Parameter')),
                ('next_level_xp', models.IntegerField(default=50, verbose_name='The number that XP (not total_XP) should be to reach the next level')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='Username')),
                ('password', models.CharField(max_length=30, verbose_name='User password')),
                ('display_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='User display name')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='I guess I should ask for an email for password recovery or something')),
                ('characters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.character')),
            ],
        ),
        migrations.CreateModel(
            name='Paradigm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Paradigm name')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Brief, optional description of Paradigm')),
                ('level', models.IntegerField(default=1, verbose_name='Experience level of this Paradigm')),
                ('xp', models.IntegerField(default=0, verbose_name='Experience points gained for this Paradigm since last level up')),
                ('total_xp', models.IntegerField(default=0, verbose_name='Total experience points gained for this Paradigm')),
                ('next_level_xp', models.IntegerField(default=50, verbose_name='The number that XP (not total_XP) should be to reach the next level')),
                ('default_parameters', models.ManyToManyField(to='core.parameter')),
            ],
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Event name')),
                ('event_date', models.DateTimeField(verbose_name='Event date and time')),
                ('significance_mod', models.IntegerField(default=1, verbose_name='A modifier representing the significance of the event; functions as a XP multiplier')),
                ('content', models.TextField(blank=True, null=True, verbose_name='The main content of the EventLog')),
                ('tagged_paradigms', models.ManyToManyField(blank=True, to='core.paradigm')),
                ('tagged_parameters', models.ManyToManyField(blank=True, to='core.parameter')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='paradigms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paradigm'),
        ),
        migrations.AddField(
            model_name='character',
            name='parameters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.parameter'),
        ),
        migrations.AddField(
            model_name='arc',
            name='event_logs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.eventlog'),
        ),
    ]
