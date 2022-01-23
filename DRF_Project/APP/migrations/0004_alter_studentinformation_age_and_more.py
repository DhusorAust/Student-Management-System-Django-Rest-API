# Generated by Django 4.0 on 2022-01-22 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_alter_studentinformation_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformation',
            name='age',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='department',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='roll',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers_related', to='APP.teacherinformation'),
        ),
    ]