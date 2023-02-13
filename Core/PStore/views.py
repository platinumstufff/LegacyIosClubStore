from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import App, News
import random

def index(reqeust):

    apps = App.objects.order_by('platform')#Get all apps

    appdata = {'apps':apps}

    return render(reqeust,'index.html',appdata)

def app_card(reqeust, app_id):

    appdata = App.objects.get(pk=app_id)#Get all app by id

    if not appdata.visible:
        return HttpResponse('Приложение скрыто')

    return render(reqeust,'cards/app_card.html',{'app':appdata})

def news(reqeust):

    news = News.objects.order_by('-date')#Get all news

    newsdata = {'news':news}

    return render(reqeust,'news.html',newsdata)

def news_card(reqeust, news_id):

    newsdata = News.objects.get(pk=news_id)

    if not newsdata.visible:
        return HttpResponse('Новость скрыта')

    return render(reqeust,'cards/news_card.html',{'news':newsdata})

def apps(reqeust):

    apps = App.objects.all()

    return render(reqeust,'apps.html',{'apps':apps})

def apps_platform(reqeust, platform):

    if not str(platform).lower() in ['android','linux','windows']:
        return HttpResponse('Platform does not exist!')

    apps_with_platform = App.objects.all()
    
    apps_with_filter = []

    for app in apps_with_platform:
        if app.platform.lower() == str(platform).lower():
            apps_with_filter.append(app)

    return render(reqeust,'index.html',{'apps':apps_with_filter})

def apps_random(reqeust):

    apps = App.objects.all()

    return render(reqeust,'cards/app_card.html',{'app':random.choice(apps)})

def apps_all(reqeust):

    apps = App.objects.all()

    data = {}

    for app in apps:
        data[app.app_id] = {
            'id':app.app_id,
            'name':app.name,
            'author':app.author
        }

    return JsonResponse(
        data
    )

def settings(reqeust):

    return render(reqeust,'settings.html')

def welcome(reqeust):

    return render(reqeust,'welcome.html')

def about(reqeust):

    return render(reqeust,'about.html')

def error_404(reqeust, exception):
    return render(reqeust, 'errors/404.html')