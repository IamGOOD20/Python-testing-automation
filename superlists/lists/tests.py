from django.test import TestCase

class HomePageTest(TestCase):
    '''Home page test'''

    def test_uses_home_template(self):
        '''Test: the home page returns correct HTML.'''

        response = self.client.get('/')
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_post_request(self):
        '''Test: can safe POST request'''
        responce = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', responce.content.decode())
        self.assertTemplateUsed(responce, 'home.html')

