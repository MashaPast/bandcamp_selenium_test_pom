from BaseApp import BasePage


class Navigation(BasePage):

    def enter_word(self, word, locator):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self, locator):
        return self.find_element(locator, time=2).click()

    def check_navigation_bar(self, locator):
        all_list = self.find_elements(locator, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def click_group(self, locator):
        return self.find_element(locator, time=2).click()

    def check_homeland(self, locator):
        homeland_list = self.find_elements(locator, time=2)
        hl_data = [x.text for x in homeland_list if len(x.text) > 0]
        return hl_data
