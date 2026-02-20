"""
Автотесты для контактной формы
"""
import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.contact_page import ContactPage


class ContactFormTests(unittest.TestCase):
    """Класс тестов для контактной формы"""
    
    @classmethod
    def setUpClass(cls):
        """
        Настройка перед запуском всех тестов
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Запуск в headless режиме
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        html_file_path = os.path.join(project_root, "contact_form.html")
        if os.name == 'nt':  # Windows
            file_url = f"file:///{html_file_path.replace(os.sep, '/')}"
        else:  # Unix/Linux/Mac
            file_url = f"file://{html_file_path}"
        
        cls.contact_page = ContactPage(cls.driver)
        cls.contact_page.open(file_url)
    
    @classmethod
    def tearDownClass(cls):
        """
        Очистка после выполнения всех тестов
        """
        cls.driver.quit()
    
    def setUp(self):
        """
        Настройка перед каждым тестом
        """
        self.driver.refresh()
    
    def test_positive_submit_form_with_all_fields(self):
        """
        Позитивный тест: заполнение всех полей формы валидными данными,
        отправка и проверка успешного сообщения
        """
        # Заполнить все поля формы валидными данными
        self.contact_page.fill_form(
            name="Иван Иванов",
            email="ivan.ivanov@example.com",
            phone="+7 (999) 123-45-67",
            message="Это тестовое сообщение для проверки формы."
        )
        
        # Отправить форму
        self.contact_page.submit_form()
        
        # Проверить, что отображается сообщение об успехе
        self.assertTrue(
            self.contact_page.is_success_message_displayed(),
            "Сообщение об успешной отправке формы не отображается"
        )
        
        # Проверить текст сообщения об успехе
        success_text = self.contact_page.get_success_message_text()
        expected_text = "Форма успешно отправлена! Спасибо за ваше сообщение."
        self.assertEqual(
            success_text,
            expected_text,
            f"Текст сообщения об успехе не соответствует ожидаемому. "
            f"Ожидалось: '{expected_text}', Получено: '{success_text}'"
        )
    
    def test_negative_submit_form_with_empty_required_field(self):
        """
        Негативный тест: попытка отправить форму с пустым обязательным полем
        и проверка текста ошибки
        """
        # Заполнить форму, оставив поле "Имя" пустым
        self.contact_page.fill_form(
            name="",
            email="test@example.com",
            phone="+7 (999) 123-45-67",
            message="Тестовое сообщение"
        )
        
        self.contact_page.submit_form()
        
        self.assertTrue(
            self.contact_page.is_name_error_displayed(),
            "Сообщение об ошибке для поля 'Имя' не отображается"
        )
        
        error_text = self.contact_page.get_name_error_text()
        expected_error = "Поле \"Имя\" обязательно для заполнения"
        self.assertEqual(
            error_text,
            expected_error,
            f"Текст ошибки не соответствует ожидаемому. "
            f"Ожидалось: '{expected_error}', Получено: '{error_text}'"
        )
        
        self.assertFalse(
            self.contact_page.is_success_message_displayed(),
            "Сообщение об успехе не должно отображаться при наличии ошибок"
        )


if __name__ == "__main__":
    unittest.main()

