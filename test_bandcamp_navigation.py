from BandcampPages import Navigation
import locators


def test_yandex_search(browser):
    bandcamp_main_page = Navigation(browser)
    bandcamp_main_page.go_to_site()
    bandcamp_main_page.enter_word("Июльские дни", locators.LOCATOR_BANDCAMP_SEARCH_FIELD)
    bandcamp_main_page.click_on_the_search_button(locators.LOCATOR_BANDCAMP_SEARCH_BUTTON)
    bandcamp_main_page.click_group(locators.LOCATOR_BANDCAMP_GROUP_BAR)
    elements = bandcamp_main_page.check_homeland(locators.LOCATOR_BANDCAMP_HOMELAND)
    new_url = browser.current_url
    assert new_url == 'https://ijulskiedni.bandcamp.com/'
    assert elements == ["Nizhny Novgorod, Russia"]