import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.web_tables_page import WebTablesPage
from utils.driver_factory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_web_tables(driver):
    page = WebTablesPage(driver)
    page.navigate()
    
    new_record = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john@example.com',
        'age': '30',
        'salary': '5000',
        'department': 'IT'
    }
    page.add_new_record(new_record)
    
    assert page.get_cell_data(4, 1) == 'John', "Novo registro não foi adicionado corretamente"
    
    edited_record = {'firstName': 'Jane'}
    page.edit_record(4, edited_record)
    
    assert page.get_cell_data(4, 1) == 'Jane', "Registro não foi editado corretamente"
    
    page.delete_record(4)
    
    assert page.get_cell_data(4, 1) == ' ', "Registro não foi deletado corretamente"
