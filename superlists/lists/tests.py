from django.test import TestCase
from lists.models import Item

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
        self.assertTemplateUsed(responce, 'lists/home.html')


class ItemModelTest(TestCase):
    '''Model test: list item'''

    def test_saving_and_retrieving_items(self):
        '''test of saving and receiving list items'''
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        print('check in ------->', saved_items)
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        print('check in ------->', first_saved_item)

        self.assertEqual(first_saved_item, 'The first (ever) list item')
        self.assertEqual(second_saved_item, 'Item the second')


