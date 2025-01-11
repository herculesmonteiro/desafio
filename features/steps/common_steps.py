from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the DemoQA homepage')
def step_impl(context):
    context.driver.get("https://demoqa.com/")

@when('I navigate to the {page_name} page')
def step_impl(context, page_name):
    element = context.driver.find_element(By.XPATH, f"//h5[text()='{page_name}']")
    element.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//span[text()='{page_name}']"))
    )
