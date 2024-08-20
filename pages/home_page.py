from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    # Şirket menü öğesinin ve kariyerler alt menüsünün lokatörleri
    NAV_ITEM_COMPANY = (By.CSS_SELECTOR, ".nav-item.dropdown:nth-of-type(6)")
    CAREERS = (By.CSS_SELECTOR, "[href='https://useinsider.com/careers/']")

    def click_nav_item_company(self):
        # Şirket menü öğesine tıklama
        self.click_element(*self.NAV_ITEM_COMPANY)

    def click_sub_item(self):
        # Kariyerler alt öğesine tıklama
        self.click_element(*self.CAREERS)
