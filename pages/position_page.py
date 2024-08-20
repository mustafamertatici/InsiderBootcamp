from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PositionPage(BasePage):
    FILTER_LOCATIONS = (By.ID, "filter-by-location")
    FILTER_ISTANBUL_TURKEY_TEXT = "Istanbul, Turkey"

    FILTER_DEPARTMENT = (By.ID, "filter-by-department")
    FILTER_QUALITY_ASSURANCE_TEXT = "Quality Assurance"

    JOBLIST = (By.ID, "jobs-list")
    JOBITEM = (By.CSS_SELECTOR, ".position-list-item")

    CONTAINERLOCATOR = (By.ID, "jobs-list")
    DEPARTMENTLOCATOR = (By.CLASS_NAME, "position-department")
    LOCATIONLOCATOR = (By.CLASS_NAME, "position-location")

    VIEWROLEBUTTON = (By.CSS_SELECTOR, ".btn.btn-navy.rounded.pt-2.pr-5.pb-2.pl-5")

    def scroll_to_location(self):
        # "Filter by Location" başlığına scroll yaparak gelir
        self.scroll_to_element(self.FILTER_LOCATIONS)

    def select_option_location_istanbul(self):
        # Lokasyon olarak "Istanbul, Turkey" seçilir.
        self.select_option_by_visible_text(self.FILTER_LOCATIONS, self.FILTER_ISTANBUL_TURKEY_TEXT)

    def select_option_departman_qualityassurance(self):
        # Departman olarak "Quality Assurance" seçilir.
        self.select_option_by_visible_text(self.FILTER_DEPARTMENT, self.FILTER_QUALITY_ASSURANCE_TEXT)

    def verify_selected_option_istanbul_turkey(self):
        # Lokasyon olarak "Istanbul, Turkey" seçildiği doğrulanır.
        self.verify_selected_option(self.FILTER_LOCATIONS, "Istanbul, Turkey", "Filter by Location")

    def verify_selected_option_quality_assurance(self):
        # Departman olarak "Quality Assurance" seçildiği doğrulanır.
        self.verify_selected_option(self.FILTER_DEPARTMENT, "Quality Assurance", "Filter by Department")

    def open_positon_number_of(self):
        # Seçimlere göre oluşan pozisyon sayısını yazar.
        self.write_result_screen(self.JOBLIST, self.JOBITEM)

    def verify_job_postings(self):
        # İş ilanlarının üzerindeki bilgilerin kontrolünü yapar
        self.check_job_postings(self.CONTAINERLOCATOR, self.DEPARTMENTLOCATOR, self.LOCATIONLOCATOR)

    def scroll_job_list(self):
        # İş ilanı listesine kaydırma yapar.
        self.scroll_to_element(self.JOBLIST)

    def click_verify_view_role_buttons_two_time(self):
        # "View Role" butonuna ilan sayısı kadar tıklar ve linklerini doğrulanır.
        self.click_verify_position_view_role_buttons(self.VIEWROLEBUTTON)
