from BandcampPages import Navigation


def test_yandex_search(browser):
    bandcamp_main_page = Navigation(browser)
    bandcamp_main_page.go_to_site()
    bandcamp_main_page.enter_word("Июльские дни")
    bandcamp_main_page.click_on_the_search_button()
    bandcamp_main_page.click_group()
    elements = bandcamp_main_page.check_homeland()
    new_url = browser.current_url
    assert new_url == 'https://ijulskiedni.bandcamp.com/'
    assert elements == ["Nizhny Novgorod, Russia"]