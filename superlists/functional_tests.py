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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''Test: you can start the list and continue it later'''
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she write in a text field "buy tools"
        # she work as a . . .
        inputbox.send_keys('Exchange laziness on brain')

        # when she click enter, the page is update and now
        # the page has "1"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Exchange laziness on brain')

            # f"The new list element did not appear in a table. It consist of:\n{table.text}")
        # The text field is proposing to add another one element
        # She inputs "To make task 2"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Start working hard')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Exchange laziness on brain')
        self.check_for_row_in_list_table('2: Start working hard')

        self.fail('End test')
        # after page update it views both elements of her list

if __name__ == '__main__':
    unittest.main(warnings='ignore')
