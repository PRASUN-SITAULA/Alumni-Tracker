# Generated by Django 2.2.3 on 2019-08-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_auto_20190818_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicstatus',
            name='details',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='areas_of_expertise',
            field=models.TextField(blank=True, null=True),
        ),
    ]
