import time
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)  # 20 saniyelik zaman aşımı

    def find(self, *locator):
        return self.driver.find_element(*locator)  # Elementi bulmak için

    def click_element(self, *locator):
        return self.driver.find_element(*locator).click()  # Bağlantı veya elemente tıklamak için

    def get_current_url(self):
        return self.driver.current_url  # O anki sayfanın URL'ini döndürür.

    def check_if_elements_clickable(self, locator, name):  # Belirtilen locator elementlerinin tıklanabilir
        elements = self.driver.find_elements(*locator)  # olup olmadığı kontrol eder
        for index, element in enumerate(elements):
            try:
                # Tıklanabilir mi kontrol et
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(element))
                print(f"{name}lardan {index + 1} nolu {name} tıklanabilir")
                # Elementi tıkla
                element.click()
                # İstege bağlı olarak işlem sonrası geri dön
                self.driver.back()

            except Exception as e:
                screenshot_name = f"{name}_{index + 1}_clickable_error.png"
                self.driver.save_screenshot(screenshot_name)
                print(
                    f"{name}lardan {index + 1} tıklanabilir değil, Hata:{str(e)}. Ekar görünütüsü alındı:{screenshot_name}")

    def check_if_elements_clickable_with_arrow(self, locator, arrow_locator, name):  # Belirtilen elementin tıklanabilir
        elements = self.driver.find_elements(*locator)  # olup olmadığı kontrol ederken
        arrow_elements = self.driver.find_element(*arrow_locator)  # arrow_locator tıklayıp.
        # elementlerin sağ kaydırılmasını sağlar.
        # Bu sayede tıklanacak locate sırası gelince ekran dışında kalmaz
        for index, element in enumerate(elements):
            try:

                # Tıklanabilir mi kontrol et
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(element))
                print(f"{name}lardan {index + 1} nolu {name} tıklanabilir")

                # Elementi tıkla
                element.click()
                time.sleep(1)
                arrow_elements.click()
                continue
            except Exception as e:
                screenshot_name = f"{name}_{index + 1}_clickable_with_arrow_error.png"
                self.driver.save_screenshot(screenshot_name)
                print(
                    f"{name}lardan {index + 1} tıklanabilir değil, Hata:{str(e)}. Ekran görüntüsü alındı: {screenshot_name}")
                continue

    def check_if_picture_elements_clickable(self, locator, name, start_index, end_index, difference_index):
        elements = self.driver.find_elements(*locator)  # Burada dikkate almamız gereken tıklamamız gereken locateler
        for index in range(start_index, end_index):  # 10 locate var bunları üçüncüden başlayım onuncu elemnte kadar
            try:  # tıklanması kontrol etmek istiyorum bunun için başlangıç, bitiş ve fark indexleri var
                element = elements[index]  # doğru locatelerin tıklanabilir kontrol etmek için

                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(element))
                print(f"{name}lardan {index - difference_index} nolu {name} tıklanabilir")
                element.click()
                time.sleep(1)
            except(TimeoutException, ElementClickInterceptedException) as e:
                screenshot_name = f"{name}_{index - difference_index}_picture_clickable_error.png"
                self.driver.save_screenshot(screenshot_name)
                print(
                    f"{name}lardan  {index - difference_index} tıklanabilir değil Hata:{str(e)},Ekran görüntüsü alındı: {screenshot_name}")
                continue

    def scroll_to_element(self, locator):  # Locate gelen web sayfasında görüntülenemiyor ise locate.
        try:
            # scroll metodu ile locate geliriz. Hata almadan süreci yürütmemezi sağlar
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as e:
            screenshot_name = f"scroll_to_element_select_error.png"
            self.driver.save_screenshot(screenshot_name)
            print(f"Elemente scroll yapılamadı, Hata:{str(e)}. Ekran görüntüsü alındı: {screenshot_name}")

    def select_option_by_visible_text(self, locator, text):  # Dropdown menüde elementi text ile seçmemizi sağlar.
        try:
            # Select elementini bul
            select_element = self.driver.find_element(*locator)

            # Select nesnesi oluşturalım
            select = Select(select_element)

            # belirtilen metne sahip seçeneği seç
            select.select_by_visible_text(text)
        except Exception as e:
            screenshot_name = f"select_option_by_visible_text_error.png"
            self.driver.save_screenshot(screenshot_name)
            print(f"Seçenek seçilemedi, Hata:{str(e)}. Ekran görüntüsü alındı:{screenshot_name}")

    def verify_selected_option(self, locator, expected_value, element_name):
        try:
            # Select elementini bul
            select_element = Select(self.driver.find_element(*locator))

            # Seçili olan option'alayım
            selected_option = select_element.first_selected_option.text.strip()

            # Seçili olan değeri kontrol et.        select elementinde seçili olan seçeneğin
            if selected_option == expected_value:  # beklenen değerle eşleşip eşleşmediği doğrulanır.
                print(f"{element_name} için doğru seçenek seçili: {selected_option}")
                return True
            else:
                print(f"{element_name} için yanlış seçenek seçildi: {selected_option}. Beklenen :{expected_value}")

        except Exception as e:
            screenshot_name = f"{element_name}verify_selected_option_error.png"
            self.driver.save_screenshot(screenshot_name)
            print(f"{element_name} doğrulaması yapılamadı, Hata:{str(e)}. Ekran görüntüsü alındı:{screenshot_name}")

    def write_result_screen(self, job_list_locator, job_item_locator):
        try:
            # kaç adet boşta pozisyon olduğunu ilanları sayarak yapar.
            job_list = self.driver.find_element(*job_list_locator)

            # Ana liste içindeki her bir iş ilanını bulalım
            job_items = job_list.find_elements(*job_item_locator)

            # İlanların sayısını alalım.
            job_count = len(job_items)

            # ilan sayısını ekrana yazdıralım
            print(f"Seçilen lokasyon ve departman için {job_count} adet boşta pozisyon var")
        except Exception as e:
            screenshot_name = f"write_result_screen_error.png"
            self.driver.save_screenshot(screenshot_name)
            print(f"Sonuç ekranı yazılamadı, Hata:{str(e)}. Ekran görüntüsü alındı:{screenshot_name}")

    def check_job_postings(self, container_locator, department_locator, location_locator):  # Her iş ilanının departman
        try:
            # ve lokasyonun doğru olup olmadığını kontrol eder.
            # iş ilanlarının bulunduğu ana container locater bulalım.
            job_list = self.driver.find_element(*container_locator)

            # iş ilanlarını bul
            job_postings = job_list.find_elements(By.CLASS_NAME, "position-list-item-wrapper.bg-light")

            for index, posting in enumerate(job_postings, start=1):
                # Departman'ı kontrol edelim
                department_text = posting.find_element(*department_locator).text
                if department_text == "Quality Assurance":
                    print(f"{index}: Departman doğru - '{department_text}'")
                else:
                    print(f"{index}: Departman yanlış - '{department_text}'")

                # location' kontrol edelim
                location_text = posting.find_element(*location_locator).text
                if location_text == "Istanbul, Turkey":
                    print(f"{index}: Lokasyon doğru - '{location_text}'")
                else:
                    print(f"{index}: Lokasyon yanlış - '{location_text}'")
        except Exception as e:
            screenshot_name = f"check_job_postings_error.png"
            self.driver.save_screenshot(screenshot_name)
            print(f"iş ilanı kontrolü yapılamadı, Hata:{str(e)}. Ekran görüntüsü alındı:{screenshot_name}")

    def click_verify_position_view_role_buttons(self, locator):
        try:

            # View Role butonlarını assign edelim.
            view_role_buttons = self.driver.find_elements(*locator)

            # Her buttona tıklayıp yeni sekmede URL kontrol edelim.
            for i, button in enumerate(view_role_buttons):
                try:
                    # Butonlar hover yapılınca gözüktü için ekleyelim
                    ActionChains(self.driver).move_to_element(button).perform()  # Butona hover yapar

                    # Butona tıklama
                    button.click()
                    print(f"{i + 1}. 'View Role' butonuna tıklandı")

                    # Yeni sekmeye geçiş yap(ikinci sekme)
                    self.driver.switch_to.window(self.driver.window_handles[-1])  # Yeni sekmeye geçiş yapar

                    # URL'yi kontrol et
                    time.sleep(2)  # Sayfanın yüklenmesi için bekleme süresi
                    current_url = self.driver.current_url

                    if "https://jobs.lever.co/" in current_url:

                        print(f"{i + 1}.nolu ilan için URL başarılı")
                    else:
                        print(f"{i + 1}.nolu ilan için URL başarılı değil")

                    # Yeni sekmeyi kapat
                    self.driver.close()

                    # ilk sekmeye geri dönelim
                    self.driver.switch_to.window(self.driver.window_handles[0])  # ilk sekmeye geri döner
                    time.sleep(2)  # sayfa geri yüklenmesi için bekleme süresi
                except Exception as e:
                    screenshot_name = f"view_role_buttons_error_{i + 1}.png"
                    self.driver.save_screenshot(screenshot_name)
                    print(f"{i + 1}. ilana tıklanmadı. Hata: {e} Ekran görüntüsü alındı: {screenshot_name}")

        except Exception as e:
            screenshot_name = f"click_verify_position_view_role_buttons_error.png"
            self.driver.save_screenshot(screenshot_name)
            print(f"View Role butonlarına erişilemedi, Hata: {e} Ekran görüntüsü alındı: {screenshot_name}")
