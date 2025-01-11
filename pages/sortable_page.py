from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class SortablePage:
    def __init__(self, driver):
        self.driver = driver
        self.sortable_items = (By.CSS_SELECTOR, ".list-group-item")

    def get_sortable_items(self):
        return self.driver.find_elements(*self.sortable_items)

    def sort_items(self):
        items = self.get_sortable_items()
        actions = ActionChains(self.driver)
        for i in range(len(items)):
            for j in range(i+1, len(items)):
                if items[i].text > items[j].text:
                    actions.drag_and_drop(items[j], items[i]).perform()
                    items = self.get_sortable_items()
