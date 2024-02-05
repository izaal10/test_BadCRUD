import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://localhost"

        self.browser.get(url)
        expected_result = "Please sign in"
        actual_result = self.browser.find_element(By.TAG_NAME, 'h1')
        
        self.assertIn(expected_result, actual_result.text)

    def test_login_with_admin_credentials(self):
        # Get the URL from the command line arguments or use a default
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://localhost"

        # Navigate to the login page
        self.browser.get(url + "/login.php")

        # Input admin credentials
        self.browser.find_element(By.ID, 'inputUsername').send_keys("admin")
        self.browser.find_element(By.ID, 'inputPassword').send_keys("admin")

        # Click the Sign in button
        self.browser.find_element(By.XPATH, '//button[text()="Sign in"]').click()

        # Check if the login was successful
        expected_result = "Welcome, admin"
        actual_result = self.browser.find_element(By.XPATH, '//h1[text()="Welcome, admin"]')
        
        self.assertIn(expected_result, actual_result.text)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'],verbosity=2,warnings='ignore')