from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os


class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        service = Service(executable_path=os.environ.get('CHROME_DRIVER_PATH'))
        cls.selenium = WebDriver(service=service)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

        # ログイン
        username_input = self.selenium.find_element(By.NAME, "login")
        username_input.send_keys(os.environ.get('TEST_USER_EMAIL'))
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys(os.environ.get('TEST_USER_PASSWORD'))
        self.selenium.find_element(By.CLASS_NAME, 'btn').click()

        # ページタイトルの検証
        self.assertEqual('日記一覧 | Private Diary', self.selenium.title)
