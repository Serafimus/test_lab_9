"""
Класс страницы контактной формы (Page Object Pattern)
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContactPage(BasePage):
    """Класс для работы с контактной формой"""
    
    # Локаторы элементов формы
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    PHONE_INPUT = (By.ID, "phone")
    MESSAGE_TEXTAREA = (By.ID, "message")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    # Локаторы сообщений
    SUCCESS_MESSAGE = (By.ID, "successMessage")
    NAME_ERROR = (By.ID, "nameError")
    EMAIL_ERROR = (By.ID, "emailError")
    MESSAGE_ERROR = (By.ID, "messageError")
    
    def __init__(self, driver):
        """
        Инициализация страницы контактов
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
    
    def fill_name(self, name):
        """
        Заполнить поле "Имя"
        
        Args:
            name: Имя для ввода
        """
        self.send_keys(self.NAME_INPUT, name)
    
    def fill_email(self, email):
        """
        Заполнить поле "Email"
        
        Args:
            email: Email для ввода
        """
        self.send_keys(self.EMAIL_INPUT, email)
    
    def fill_phone(self, phone):
        """
        Заполнить поле "Телефон"
        
        Args:
            phone: Телефон для ввода
        """
        self.send_keys(self.PHONE_INPUT, phone)
    
    def fill_message(self, message):
        """
        Заполнить поле "Сообщение"
        
        Args:
            message: Сообщение для ввода
        """
        self.send_keys(self.MESSAGE_TEXTAREA, message)
    
    def submit_form(self):
        """
        Отправить форму
        """
        self.click(self.SUBMIT_BUTTON)
    
    def fill_form(self, name="", email="", phone="", message=""):
        """
        Заполнить всю форму
        
        Args:
            name: Имя
            email: Email
            phone: Телефон (опционально)
            message: Сообщение
        """
        if name:
            self.fill_name(name)
        if email:
            self.fill_email(email)
        if phone:
            self.fill_phone(phone)
        if message:
            self.fill_message(message)
    
    def is_success_message_displayed(self):
        """
        Проверить, отображается ли сообщение об успехе
        
        Returns:
            bool: True если сообщение видно, False иначе
        """
        return self.is_element_visible(self.SUCCESS_MESSAGE)
    
    def get_success_message_text(self):
        """
        Получить текст сообщения об успехе
        
        Returns:
            str: Текст сообщения
        """
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def is_name_error_displayed(self):
        """
        Проверить, отображается ли ошибка для поля "Имя"
        
        Returns:
            bool: True если ошибка видна, False иначе
        """
        return self.is_element_visible(self.NAME_ERROR)
    
    def get_name_error_text(self):
        """
        Получить текст ошибки для поля "Имя"
        
        Returns:
            str: Текст ошибки
        """
        return self.get_text(self.NAME_ERROR)
    
    def is_email_error_displayed(self):
        """
        Проверить, отображается ли ошибка для поля "Email"
        
        Returns:
            bool: True если ошибка видна, False иначе
        """
        return self.is_element_visible(self.EMAIL_ERROR)
    
    def get_email_error_text(self):
        """
        Получить текст ошибки для поля "Email"
        
        Returns:
            str: Текст ошибки
        """
        return self.get_text(self.EMAIL_ERROR)
    
    def is_message_error_displayed(self):
        """
        Проверить, отображается ли ошибка для поля "Сообщение"
        
        Returns:
            bool: True если ошибка видна, False иначе
        """
        return self.is_element_visible(self.MESSAGE_ERROR)
    
    def get_message_error_text(self):
        """
        Получить текст ошибки для поля "Сообщение"
        
        Returns:
            str: Текст ошибки
        """
        return self.get_text(self.MESSAGE_ERROR)

