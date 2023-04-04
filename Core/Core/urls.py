from django.contrib import admin
from django.urls import path
import PStore.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', PStore.views.index),
    path('welcome/', PStore.views.welcome),
    path('news/', PStore.views.news),
    path('settings/', PStore.views.settings),
    path('about/', PStore.views.about),
    path('app/<int:app_id>/', PStore.views.app_card, name='app_card'),
    path('apps/', PStore.views.apps),
    path('apps/random/', PStore.views.apps_random),
    path('apps/all/', PStore.views.apps_all),
    path('apps/platform/<str:platform>/', PStore.views.apps_platform, name='platform'),
    path('news/<int:news_id>/', PStore.views.news_card, name='news_card'),
]


handler404 = 'PStore.views.error_404'
