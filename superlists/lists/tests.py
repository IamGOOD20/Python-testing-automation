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

    def test_can_save_a_POST_request(self):
        '''Test: can safe POST request'''
        responce = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        '''Test: redirect after POST'''
        responce = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(responce.status_code, 302)
        self.assertEqual(responce['location'], '/')

    def test_only_saves_items_when_necessary(self):
        '''Test: saves elements when it necessary'''
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_display_all_list_items(self):
        '''Test: Display all list items'''
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        responce = self.client.get('/')

        self.assertIn('item 1', responce.content.decode)
        self.assertIn('item 2', responce.content.decode)

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
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


