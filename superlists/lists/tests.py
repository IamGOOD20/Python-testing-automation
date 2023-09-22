from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        '''тест: корневой url преобразуется в представление домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

# class HomePageTest(TestCase):
#     '''Test home page'''
#
#     def test_uses_home_templates(self):
#         '''Test: using home template'''
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'lists/home.html')
#
#
#     def test_home_page_returns_correct_html(self):
#         '''Test: the home page return correct html'''
#
#         response = self.client.get('/')
#         html = response.content.decode('utf8')
#
#         self.assertTrue(html.startswith('<html>'))
#         self.assertIn('<title>To-Do lists</title>', html)
#         self.assertTrue(html.strip().endswith('</html>'))
#         self.assertTemplateUsed(response, 'lists/home.html')

