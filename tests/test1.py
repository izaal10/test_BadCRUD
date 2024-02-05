import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        # Ensure that the page is loaded before each test
        url = os.environ.get("URL")  # Retrieve the URL from environment variables
        if not url:
            raise ValueError("URL not provided in environment variables")
        self.driver.get(url)

    def test_valid_login(self):
        self.login("admin", "admin")
        expected_url = os.environ.get("EXPECTED_URL", "http://localhost/index.php")
        self.assertIn(expected_url, self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login(self, username, password):
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
