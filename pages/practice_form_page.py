from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
        
    def navigate(self):
        self.driver.get(self.url)
        
    def fill_form(self, data):
        self.driver.find_element(By.ID, "firstName").send_keys(data['firstName'])
        self.driver.find_element(By.ID, "lastName").send_keys(data['lastName'])
        self.driver.find_element(By.ID, "userEmail").send_keys(data['email'])
        self.driver.find_element(By.CSS_SELECTOR, f"label[for='gender-radio-{data['gender']}']").click()
        self.driver.find_element(By.ID, "userNumber").send_keys(data['mobile'])
        
        # Date of Birth
        self.driver.find_element(By.ID, "dateOfBirthInput").click()
        month_select = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        month_select.select_by_visible_text(data['month'])
        year_select = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        year_select.select_by_value(data['year'])
        self.driver.find_element(By.CSS_SELECTOR, f".react-datepicker__day--0{data['day']}").click()
        
        # Subjects
        subjects_input = self.driver.find_element(By.ID, "subjectsInput")
        for subject in data['subjects']:
            subjects_input.send_keys(subject)
            subjects_input.send_keys(Keys.ENTER)
        
        # Hobbies
        for hobby in data['hobbies']:
            self.driver.find_element(By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{hobby}']").click()
        
        # Picture
        self.driver.find_element(By.ID, "uploadPicture").send_keys(data['picture_path'])
        
        self.driver.find_element(By.ID, "currentAddress").send_keys(data['currentAddress'])
        
        # State and City
        state_input = self.driver.find_element(By.ID, "react-select-3-input")
        state_input.send_keys(data['state'])
        state_input.send_keys(Keys.ENTER)
        
        city_input = self.driver.find_element(By.ID, "react-select-4-input")
        city_input.send_keys(data['city'])
        city_input.send_keys(Keys.ENTER)
        
    def submit_form(self):
        self.driver.find_element(By.ID, "submit").click()
        
    def is_popup_visible(self):
        return self.driver.find_element(By.CLASS_NAME, "modal-content").is_displayed()
        
    def close_popup(self):
        self.driver.find_element(By.ID, "closeLargeModal").click()
