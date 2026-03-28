from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    SEARCH_BOX = (By.CLASS_NAME, "product_sort_container")  
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def search_product(self, keyword):
       
        self.keyword = keyword.lower()

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        names = [el.text for el in elements]

        if hasattr(self, "keyword") and self.keyword:
            return [n for n in names if self.keyword in n.lower()]

        return names
