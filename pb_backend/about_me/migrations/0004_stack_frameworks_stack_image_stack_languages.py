# Generated by Django 4.2.6 on 2023-11-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frameworks', '0001_initial'),
        ('languages', '0001_initial'),
        ('about_me', '0003_delete_framework'),
    ]

    operations = [
        migrations.AddField(
            model_name='stack',
            name='frameworks',
            field=models.ManyToManyField(to='frameworks.framework'),
        ),
        migrations.AddField(
            model_name='stack',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='stack',
            name='languages',
            field=models.ManyToManyField(to='languages.language'),
        ),
    ]
