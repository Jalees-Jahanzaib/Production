# Generated by Django 3.0 on 2020-01-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200102_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='upload',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
