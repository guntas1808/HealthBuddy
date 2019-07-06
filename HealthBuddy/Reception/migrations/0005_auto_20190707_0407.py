# Generated by Django 2.2.2 on 2019-07-06 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reception', '0004_auto_20190706_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient_roll',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='receptionist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Reception.Reception'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('w', 'Waiting'), ('e', 'Examining'), ('t', 'Terminated')], default='w', max_length=2),
        ),
    ]
