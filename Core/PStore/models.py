from django.db import models
from django.utils.translation import gettext as _
import datetime

#App model
class App(models.Model):
    name = models.CharField(default='App', max_length=100, help_text='Укажите название приложения')
    app_id = models.AutoField(primary_key=True)
    author = models.CharField(default='Dev', help_text='Введите разработчика',max_length=50)
    description = models.TextField(default='Ничего', help_text='Введите описание приложения')
    link = models.CharField(default='APP.APK',max_length=300, help_text='Укажите путь к приложению')
    image = models.CharField(default='noimage.png',max_length=300, help_text='Укажите путь к картинке (noimage.png стандартная картинка)')


    CHOICES_PLATFORM = [
        ('OS', (
                ('Windows', 'Windows'),
                ('Android','Android'),
                ('Linux', 'Linux'),
            )
        )]

    platform = models.CharField(max_length=300, choices = CHOICES_PLATFORM, default=None, help_text='Укажите платформу')

    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("app_id",)


#News model
class News(models.Model):
    title = models.CharField(default='Чета случилось', max_length=100, help_text='Введите название новости')
    news_id = models.AutoField(primary_key=True)
    text = models.TextField(default='Стор удалён, пон.', help_text='Введите текст новости')
    date = models.DateField(_("Date"), default=datetime.date.today, help_text='Укажите дату новости')

    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('news_id',)

    def __str__(self):
        return self.title