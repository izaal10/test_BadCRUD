import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_valid_login(self):
            self.login("admin", "admin")
            self.assertIn("http://localhost:4444/index.php", self.driver.current_url)

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')