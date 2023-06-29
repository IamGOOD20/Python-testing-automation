from django.test import TestCase
<<<<<<< HEAD
=======
from django.http import HttpRequest

from .views import home_page
from django.template.loader import render_to_string
>>>>>>> 27584023c165e7a7f0b8b8690c84744917ad1cf5

class HomePageTest(TestCase):
    '''тест домашней страницы'''

    def test_uses_home_templates(self):
        '''тест: использеутся домашний шаблон'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')


    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''

        response = self.client.get('/')
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
<<<<<<< HEAD
=======

>>>>>>> 27584023c165e7a7f0b8b8690c84744917ad1cf5
        self.assertTemplateUsed(response, 'lists/home.html')