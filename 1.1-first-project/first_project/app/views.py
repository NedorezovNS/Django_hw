import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg = (f'Текущее время: {current_time:{"%H:%M:%S"}}'
           f'<br /><br /><a href={reverse("home")}> Вернуться на главную страницу</a>')
    return HttpResponse(msg)


def workdir_view(request):
    workdir = '<br />'.join(os.listdir('.'))
    response = (f'Содержимое рабочей дирректории:<br />{workdir}'
                f'<br /><br /><a href={reverse("home")}> Вернуться на главную страницу</a>')
    return HttpResponse(response)
