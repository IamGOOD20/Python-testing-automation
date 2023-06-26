from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import home_page
from django.template.loader import render_to_string

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

        self.assertTemplateUsed(response, 'lists/home.html')