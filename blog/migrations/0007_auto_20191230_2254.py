# Generated by Django 3.0 on 2019-12-30 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191230_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='Roles',
            field=models.CharField(choices=[('S', 'Scan'), ('1', 'Phase 1'), ('2', 'Phase 2'), ('3', 'Phase 3'), ('F', 'Final')], default='Scan', max_length=10),
        ),
    ]
