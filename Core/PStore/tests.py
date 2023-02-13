from django.urls import reverse, URLPattern
from Core.urls import urlpatterns
from django.test import TestCase
from .models import App
#Test pages

class AppTestCase(TestCase):
    def setUp(self):
        App.objects.create(name="Test App", platform="Windows")
        App.objects.create(name="Test App 2", platform="Android")

    def test_app(self):
        app = App.objects.get(name="Test App")
        app2 = App.objects.get(name="Test App 2")

        self.assertTrue(isinstance(app, App))
        self.assertTrue(isinstance(app2, App))
        
        self.assertEqual(app.__str__(), app.name)
        self.assertEqual(app2.__str__(), app2.name)

class UrlsTest(TestCase):
    def test_responses(self):
        for url in urlpatterns:
            
            if not isinstance(url, URLPattern) or url.pattern.regex.groups or not url.name:
                continue
            
            urlpath = reverse(url.name)
            response = self.client.get(urlpath, follow=True)
            self.assertEqual(response.status_code, 200)