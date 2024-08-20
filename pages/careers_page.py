from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CareersPage(BasePage):
    REJECT = (By.CSS_SELECTOR, '[id="wt-cli-reject-btn"]')

    TEAMS = (By.CSS_SELECTOR, "[class='job-item col-12 col-lg-4 mt-5']")
    TEAMONEHeader = (By.XPATH, "//h3[normalize-space()='Find your calling']")

    LOCATIONSHEADER = (By.CSS_SELECTOR, ".category-title-media.ml-0")
    LOCATIONS = (By.CSS_SELECTOR, "ul.glide__slides > li")
    LOCATIONS_ARROW = (By.CSS_SELECTOR, "[class='icon-arrow-right location-slider-next ml-4 text-xsmall text-dark']")

    PICTURESLIDER = (By.CSS_SELECTOR, '[class="elementor-swiper"]')
    PICTURES = (By.CSS_SELECTOR, '.swiper-slide')

    def scroll_see_teams(self):
        # "Find your calling" başlığına kaydırma
        self.scroll_to_element(self.TEAMONEHeader)

    def check_clickability_team_members(self):
        # Tüm takım üyelelerinin tıklanabilirliğini kontrol etme
        self.check_if_elements_clickable(self.TEAMS, "takım")

    def scroll_see_location(self):
        # Lokasyon başlığına kaydırma
        self.scroll_to_element(self.LOCATIONSHEADER)

    def cheeck_clickability_all_our_locations(self):
        # Tüm lokasyonların tıklanabilirliğini kontrol etme
        self.check_if_elements_clickable_with_arrow(self.LOCATIONS, self.LOCATIONS_ARROW, "lokasyon")

    def scroll_see_picture_header(self):
        # Resim slider alanına kaydırma
        self.scroll_to_element(self.PICTURESLIDER)

    def cheeck_clickability_life_at_insider_pictures(self):
        # Resimlerin tıklanabilirliğini kontrol etme
        self.check_if_picture_elements_clickable(self.PICTURES, "fotoraf", 4, 11, 3)

    def click_cookies_reject(self):
        # Çerezleri reddetme butonuna tıklama
        self.click_element(*self.REJECT)

    def click_new_quality_assurance_page(self):
        # Yeni "Quality Assurance" sayfasına gitme
        new_page = "https://useinsider.com/careers/quality-assurance/"
        self.driver.get(new_page)
