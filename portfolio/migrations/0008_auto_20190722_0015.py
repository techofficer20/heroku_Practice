# Generated by Django 2.2.3 on 2019-07-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20190722_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='../media/images/'),
        ),
    ]