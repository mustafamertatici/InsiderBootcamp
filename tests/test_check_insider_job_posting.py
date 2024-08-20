from pages.careers_page import CareersPage
from pages.position_page import PositionPage
from pages.quality_assurance_page import QualityAssurancePage
from tests.base_test import BaseTest
import time
from pages.home_page import HomePage


class TestCheckInsiderJobPosting(BaseTest):
    def test_something(self):
        home_page = HomePage(self.driver)
        self.assertEqual(self.base_url, home_page.get_current_url(),
                         "Insider Anasayfası açılmadı")
        home_page.click_nav_item_company()
        home_page.click_sub_item()
        careers_page = CareersPage(self.driver)

        time.sleep(1)
        careers_page.click_cookies_reject()

        careers_page.scroll_see_teams()
        time.sleep(4)
        careers_page.check_clickability_team_members()
        time.sleep(2)
        careers_page.scroll_see_location()
        time.sleep(2)
        careers_page.cheeck_clickability_all_our_locations()
        time.sleep(2)
        careers_page.scroll_see_picture_header()
        time.sleep(2)
        careers_page.cheeck_clickability_life_at_insider_pictures()
        time.sleep(2)

        careers_page.click_new_quality_assurance_page()

        qualityassurance_page = QualityAssurancePage(self.driver)
        qualityassurance_page.click_see_all_qa_jobs_button()

        positionpage = PositionPage(self.driver)
        positionpage.scroll_to_location()
        positionpage.select_option_location_istanbul()
        time.sleep(2)
        positionpage.verify_selected_option_istanbul_turkey()
        positionpage.select_option_departman_qualityassurance()
        time.sleep(2)
        positionpage.verify_selected_option_quality_assurance()
        time.sleep(4)
        positionpage.open_positon_number_of()
        positionpage.verify_job_postings()
        positionpage.scroll_job_list()
        time.sleep(2)
        positionpage.click_verify_view_role_buttons_two_time()
        time.sleep(2)
