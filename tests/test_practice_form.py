import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.practice_form_page import PracticeFormPage
from utils.driver_factory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_practice_form(driver):
    page = PracticeFormPage(driver)
    page.navigate()
    
    # Leia os dados do arquivo
    with open('data/form_data.txt', 'r') as file:
        data = eval(file.read())
    
    page.fill_form(data)
    page.submit_form()
    
    assert page.is_popup_visible(), "Popup não foi exibido após o envio do formulário"
    
    page.close_popup()
