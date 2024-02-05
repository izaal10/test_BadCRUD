import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        # Ensure that the page is loaded before each test
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_valid_login(self):
        self.login("admin", "admin")
        self.assertIn("http://localhost:4444/index.php", self.driver.current_url)

    def test_invalid_login(self):
        self.login("invalid_user", "invalid_password")
        error_message = self.driver.find_element(By.XPATH, "//div[@class='checkbox mb-3']/label").text
        self.assertEqual(error_message, "Wrong usename or password")

    def test_empty_credentials(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        submit_button.click()
        form_heading = self.driver.find_element(By.XPATH, "//form/h1").text
        self.assertEqual(form_heading, "Please sign in")

    def tearDown(self):
        # Optional: You can add cleanup logic here if needed
        pass

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
