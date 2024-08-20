from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class QualityAssurancePage(BasePage):
    SEE_ALL_QA_JOBS = (By.CSS_SELECTOR, ".btn.btn-outline-secondary")

    def click_see_all_qa_jobs_button(self):
        # "See All QA Jobs" butonuna tıklama
        self.click_element(*self.SEE_ALL_QA_JOBS)
