from BaseApp import BasePage
from selenium.webdriver.common.by import By

class BandcampLocators:
    LOCATOR_BANDCAMP_SEARCH_FIELD = (By.CSS_SELECTOR, "#autocomplete-form > input.you-autocomplete-me.dismiss-tooltip-alt")
    LOCATOR_BANDCAMP_SEARCH_BUTTON = (By.CSS_SELECTOR, "#autocomplete-form > button > svg")
    LOCATOR_BANDCAMP_NAVIGATION_BAR = (By.CSS_SELECTOR, "#pgBd > div.search > div.leftcol > div > ul > li.searchresult.band > div > div.heading > a")
    LOCATOR_BANDCAMP_HOMELAND = (By.CSS_SELECTOR, "#band-name-location > span.location.secondaryText")

class Navigation(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(BandcampLocators.LOCATOR_BANDCAMP_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(BandcampLocators.LOCATOR_BANDCAMP_SEARCH_BUTTON, time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(BandcampLocators.LOCATOR_BANDCAMP_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def click_group(self):
        return self.find_element(BandcampLocators.LOCATOR_BANDCAMP_NAVIGATION_BAR, time=2).click()

    def check_homeland(self):
        homeland_list = self.find_elements(BandcampLocators.LOCATOR_BANDCAMP_HOMELAND, time=2)
        hl_data = [x.text for x in homeland_list if len(x.text) > 0]
        return hl_data
