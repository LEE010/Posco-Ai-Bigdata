# Generated by Django 2.1.5 on 2019-02-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('time', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
            ],
        ),
    ]
