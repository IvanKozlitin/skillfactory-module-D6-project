# Generated by Django 3.0.4 on 2020-11-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='age',
            field=models.SmallIntegerField(blank=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.CharField(blank=True, max_length=150, verbose_name='Порода'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='gender',
            field=models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], default='Мальчик', max_length=7, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='kind_of_animal',
            field=models.CharField(choices=[('CAT', 'Кошка'), ('DOG', 'Собака')], default='CAT', max_length=3, verbose_name='Разновидность животного'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(blank=True, upload_to='animals_photo/%Y/%m/%d', verbose_name='Загрузить фото'),
        ),
    ]
