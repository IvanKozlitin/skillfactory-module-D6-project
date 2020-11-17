from django.contrib import admin
from .models import (Animal)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind_of_animal', 'gender', 'age', 'receipt_date', 'image_img',)
    list_filter = ('kind_of_animal', 'gender', 'age')
    readonly_fields = ['image_img', ]
