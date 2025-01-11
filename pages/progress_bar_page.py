from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProgressBarPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/progress-bar"
        
    def navigate(self):
        self.driver.get(self.url)
        
    def start_progress(self):
        self.driver.find_element(By.ID, "startStopButton").click()
        
    def stop_progress(self):
        self.driver.find_element(By.ID, "startStopButton").click()
        
    def reset_progress(self):
        self.driver.find_element(By.ID, "resetButton").click()
        
    def get_progress_value(self):
        progress_bar = self.driver.find_element(By.CLASS_NAME, "progress-bar")
        return int(progress_bar.get_attribute("aria-valuenow"))
        
    def wait_for_progress(self, target_value):
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "progress-bar"), f"{target_value}%")
        )
