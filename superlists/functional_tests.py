from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    '''New user test'''

    def setUp(self):
        '''connection to Chrome'''
        self.browser = webdriver.Chrome()

    def tearDown(self):
        '''disconnect Chrome'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''Test: you can start the list and continue it later'''
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.NAME, 'h1').text
        self.assertIn('To-Do', header_text)





        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )


        inputbox.send_keys('Buy something')


        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy new item' for row in rows),
            "The new list element did not appear"
        )


        self.fail('End test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
