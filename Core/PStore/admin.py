from django.contrib import admin
from .models import App, News

# Apps

# Hide apps action


@admin.action(description='Mark selected apps as hidden')
def apps_make_hidden(modeladmin, request, queryset):
    queryset.update(visible=False)
# Unhide apps action


@admin.action(description='Mark selected apps as visible')
def apps_make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)


class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'app_id', 'author')
    actions = [apps_make_hidden, apps_make_visible]


admin.site.register(App, AppAdmin)  # Register model App
# End apps

# News
# Hide news action


@admin.action(description='Mark selected news as hidden')
def news_make_hidden(modeladmin, request, queryset):
    queryset.update(visible=False)
# Unhide news action


@admin.action(description='Mark selected news as visible')
def news_make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_id', 'date')
    actions = [news_make_hidden, news_make_visible]


admin.site.register(News, NewsAdmin)  # Register model News
# End news
