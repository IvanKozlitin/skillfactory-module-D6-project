from django.db import models


class Animal(models.Model):
    ANIMAL_KIND_CHOICES = [
        ("CAT", "Кошка"),
        ("DOG", "Собака"),
    ]
    kind_of_animal = models.CharField(
        max_length=3,
        choices=ANIMAL_KIND_CHOICES,
        default="CAT",
        verbose_name="Разновидность животного",
    )
    name = models.CharField(max_length=100, verbose_name="Кличка")
    breed = models.CharField(blank=True, null=True, max_length=150, verbose_name="Порода")
    description = models.TextField(verbose_name="Описание")
    age = models.SmallIntegerField(blank=True, null=True, verbose_name="Возраст")
    receipt_date = models.DateField(verbose_name="Дата поступления")
    ANIMAL_GENDER_CHOICES = [
        ("Мальчик", "Мальчик"),
        ("Девочка", "Девочка"),
    ]
    gender = models.CharField(
        max_length=7,
        choices=ANIMAL_GENDER_CHOICES,
        default="Мальчик",
        verbose_name="Пол",
    )
    photo = models.ImageField(upload_to="animals_photo/%Y/%m/%d", blank=True, null=True, verbose_name="Загрузить фото")

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"

    # Вывод картинок в админке
    def image_img(self):
        if self.photo:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="75"/></a>'.format(self.photo.url))
        else:
            return "(Нет фотографии)"
    image_img.short_description = "Фото"
    image_img.allow_tags = True
