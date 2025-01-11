from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserWindowsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/browser-windows"
        
    def navigate(self):
        self.driver.get(self.url)
        
    def click_new_window_button(self):
        self.driver.find_element(By.ID, "windowButton").click()
        
    def switch_to_new_window(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        
    def get_new_window_text(self):
        return self.driver.find_element(By.ID, "sampleHeading").text
        
    def close_new_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
