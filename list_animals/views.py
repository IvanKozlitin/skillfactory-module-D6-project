from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.shortcuts import redirect
from list_animals.models import Animal


class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal_data"] = Animal.objects.all()
        context["title"] = "Приют домашних животных - Главная страница"
        return context


class ListAnimalsPageView(ListView):
    template_name = "list_animals.html"
    model = Animal
    paginate_by = 6
    context_object_name = "animal_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Приют домашних животных - Список животных"
        return context


class DetailAnimalPageView(DetailView):
    template_name = "animal_detail.html"
    model = Animal
    context_object_name = "animal_data"


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Приют домашних животных - Контакты"
        return context
