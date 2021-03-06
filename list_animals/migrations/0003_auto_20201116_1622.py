# Generated by Django 3.0.4 on 2020-11-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_animals', '0002_auto_20201116_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='age',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Порода'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='animals_photo/%Y/%m/%d', verbose_name='Загрузить фото'),
        ),
    ]
