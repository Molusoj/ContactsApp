# Generated by Django 2.2 on 2019-08-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20190811_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('undisclosed', 'Undisclosed')], default='Undisclosed', max_length=50),
        ),
    ]
