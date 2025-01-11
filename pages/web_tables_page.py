from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/webtables"
        
    def navigate(self):
        self.driver.get(self.url)
        
    def add_new_record(self, data):
        self.driver.find_element(By.ID, "addNewRecordButton").click()
        self.driver.find_element(By.ID, "firstName").send_keys(data['firstName'])
        self.driver.find_element(By.ID, "lastName").send_keys(data['lastName'])
        self.driver.find_element(By.ID, "userEmail").send_keys(data['email'])
        self.driver.find_element(By.ID, "age").send_keys(data['age'])
        self.driver.find_element(By.ID, "salary").send_keys(data['salary'])
        self.driver.find_element(By.ID, "department").send_keys(data['department'])
        self.driver.find_element(By.ID, "submit").click()
        
    def edit_record(self, row, new_data):
        self.driver.find_element(By.ID, f"edit-record-{row}").click()
        self.driver.find_element(By.ID, "firstName").clear()
        self.driver.find_element(By.ID, "firstName").send_keys(new_data['firstName'])
        self.driver.find_element(By.ID, "submit").click()
        
    def delete_record(self, row):
        self.driver.find_element(By.ID, f"delete-record-{row}").click()
        
    def get_cell_data(self, row, column):
        return self.driver.find_element(By.XPATH, f"//div[@class='rt-tbody']/div[{row}]/div/div[{column}]").text
