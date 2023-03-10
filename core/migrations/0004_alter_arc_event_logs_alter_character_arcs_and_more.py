# Generated by Django 4.1.4 on 2023-03-11 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_arc_event_logs_alter_character_arcs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arc',
            name='event_logs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.eventlog'),
        ),
        migrations.AlterField(
            model_name='character',
            name='arcs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.arc'),
        ),
        migrations.AlterField(
            model_name='character',
            name='paradigms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.paradigm'),
        ),
        migrations.AlterField(
            model_name='character',
            name='parameters',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.parameter'),
        ),
        migrations.AlterField(
            model_name='user',
            name='characters',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.character'),
        ),
    ]
