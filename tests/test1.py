import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        option = webdriver.FirefoxOptions()
        option.add_argument('--ignore-ssl-errors=yes')
        option.add_argument('--ignore-certificate-errors')
        self.browser = webdriver.Remote(options=option)

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
        # Navigate to the login page
        self.browser.get("http://localhost/login.php")

        # Input admin credentials
        self.browser.find_element(By.ID, 'inputUsername').send_keys("admin")
        self.browser.find_element(By.ID, 'inputPassword').send_keys("admin")

        # Click the Sign in button
        self.browser.find_element(By.TAG_NAME, 'button"]').click()

    

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore')