"""
Базовый класс для всех страниц (Page Object Pattern)
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, driver):
        """
        Инициализация базовой страницы
        
        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, url):
        """
        Открыть страницу по URL
        
        Args:
            url: URL страницы для открытия
        """
        self.driver.get(url)
    
    def find_element(self, locator):
        """
        Найти элемент на странице
        
        Args:
            locator: Кортеж (By, значение)
            
        Returns:
            WebElement: Найденный элемент
        """
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """
        Найти все элементы на странице
        
        Args:
            locator: Кортеж (By, значение)
            
        Returns:
            List[WebElement]: Список найденных элементов
        """
        return self.driver.find_elements(*locator)
    
    def wait_for_element(self, locator, timeout=10):
        """
        Ожидать появления элемента на странице
        
        Args:
            locator: Кортеж (By, значение)
            timeout: Время ожидания в секундах
            
        Returns:
            WebElement: Найденный элемент
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_element_visible(self, locator, timeout=10):
        """
        Ожидать видимости элемента на странице
        
        Args:
            locator: Кортеж (By, значение)
            timeout: Время ожидания в секундах
            
        Returns:
            WebElement: Найденный элемент
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator, timeout=10):
        """
        Ожидать кликабельности элемента
        
        Args:
            locator: Кортеж (By, значение)
            timeout: Время ожидания в секундах
            
        Returns:
            WebElement: Найденный элемент
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def is_element_present(self, locator):
        """
        Проверить наличие элемента на странице
        
        Args:
            locator: Кортеж (By, значение)
            
        Returns:
            bool: True если элемент присутствует, False иначе
        """
        try:
            self.find_element(locator)
            return True
        except:
            return False
    
    def is_element_visible(self, locator):
        """
        Проверить видимость элемента на странице
        
        Args:
            locator: Кортеж (By, значение)
            
        Returns:
            bool: True если элемент видим, False иначе
        """
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def get_text(self, locator):
        """
        Получить текст элемента
        
        Args:
            locator: Кортеж (By, значение)
            
        Returns:
            str: Текст элемента
        """
        element = self.find_element(locator)
        return element.text
    
    def click(self, locator):
        """
        Кликнуть по элементу
        
        Args:
            locator: Кортеж (By, значение)
        """
        element = self.wait_for_element_clickable(locator)
        element.click()
    
    def send_keys(self, locator, text):
        """
        Ввести текст в поле
        
        Args:
            locator: Кортеж (By, значение)
            text: Текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_title(self):
        """
        Получить заголовок страницы
        
        Returns:
            str: Заголовок страницы
        """
        return self.driver.title

