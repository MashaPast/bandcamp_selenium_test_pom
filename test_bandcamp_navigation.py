from BandcampPages import SearchPage, SearchResultsPage
import locators


def test_bandcamp_search(browser):
    bandcamp_main_page = SearchPage(browser)
    bandcamp_main_page.go_to_site()
    bandcamp_main_page.enter_word("Июльские дни", locators.LOCATOR_BANDCAMP_SEARCH_FIELD)
    bandcamp_main_page.click_on_the_search_button(locators.LOCATOR_BANDCAMP_SEARCH_BUTTON)

    search_results_page = SearchResultsPage(browser)
    search_results_page.click_group(locators.LOCATOR_BANDCAMP_GROUP_BAR)
    elements = search_results_page.check_homeland(locators.LOCATOR_BANDCAMP_HOMELAND)
    new_url = browser.current_url
    assert new_url == 'https://ijulskiedni.bandcamp.com/'
    assert elements == ["Nizhny Novgorod, Russia"]