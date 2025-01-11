import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.browser_windows_page import BrowserWindowsPage
from utils.driver_factory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_browser_windows(driver):
    page = BrowserWindowsPage(driver)
    page.navigate()
    page.click_new_window_button()
    page.switch_to_new_window()
    
    assert page.get_new_window_text() == "This is a sample page", "O texto na nova janela não corresponde ao esperado"
    
    page.close_new_window()
