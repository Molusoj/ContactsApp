# Generated by Django 2.2 on 2019-08-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='contact-image')),
                ('name', models.CharField(max_length=150)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
