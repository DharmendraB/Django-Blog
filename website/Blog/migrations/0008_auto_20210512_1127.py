# Generated by Django 3.1.5 on 2021-05-12 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_postcommet'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.category'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='post_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.tag'),
        ),
    ]
