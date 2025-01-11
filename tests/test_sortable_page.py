import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.sortable_page import SortablePage
from utils.driver_factory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_sortable(driver):
    page = SortablePage(driver)
    driver.get("https://demoqa.com/sortable")
    page.sort_items()
    
    sorted_items = page.get_sortable_items()
    sorted_texts = [item.text for item in sorted_items]
    assert sorted_texts == sorted(sorted_texts)
