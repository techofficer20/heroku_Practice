# Generated by Django 2.2.3 on 2019-07-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190721_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
