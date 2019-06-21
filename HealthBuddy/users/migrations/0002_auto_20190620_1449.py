# Generated by Django 2.2.2 on 2019-06-20 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNo', models.CharField(max_length=15)),
                ('timings', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='HCDept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('remarks', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Doctor')),
                ('medicines', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Medicines')),
                ('tests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tests')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('bloodGroup', models.CharField(max_length=10)),
                ('drugAllergies', models.CharField(max_length=500)),
                ('significantMedicalHistory', models.CharField(max_length=5000)),
                ('phoneNo', models.CharField(max_length=15)),
                ('emergencyContactName', models.CharField(max_length=50)),
                ('emergencyContactNo', models.CharField(max_length=15)),
                ('rollNo', models.CharField(max_length=15)),
                ('dependentName', models.CharField(max_length=50)),
                ('dependentRelation', models.CharField(max_length=15)),
                ('designation', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=15)),
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Prescription')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.HCDept'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doctor',
            name='visitDays',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Days'),
        ),
        migrations.CreateModel(
            name='bodyVitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodPressure', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('height', models.CharField(max_length=10)),
                ('sugarLevel', models.CharField(max_length=20)),
                ('prescription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Prescription')),
            ],
        ),
    ]
