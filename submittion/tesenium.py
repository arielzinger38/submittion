import unittest
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By


class TestWebPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "http://localhost"  # Replace with the actual URL

    def test_web_page_served_correctly(self):
        self.driver.get(self.url)
        self.assertTrue(self.driver.title, "Page title is empty")

    def test_date_presented(self):
        self.driver.get(self.url)
        date_element = self.driver.find_element(By.ID, "date")
        self.assertTrue(date_element.text, "Date element is empty")

    def test_date_is_current_date(self):
        self.driver.get(self.url)
        date_element = self.driver.find_element(By.ID, "date")
        date_text = date_element.text
        expected_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.assertEqual(date_text, f"Current Date and Time: {expected_date}", "Date is not the current date and time")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
