# Generated by Django 3.1.5 on 2021-05-12 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=60)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
