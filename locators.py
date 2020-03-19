from selenium.webdriver.common.by import By


LOCATOR_BANDCAMP_SEARCH_FIELD = (By.CSS_SELECTOR, "#autocomplete-form > input.you-autocomplete-me.dismiss-tooltip-alt")
LOCATOR_BANDCAMP_SEARCH_BUTTON = (By.CSS_SELECTOR, "#autocomplete-form > button > svg")
LOCATOR_BANDCAMP_GROUP_BAR = (By.CSS_SELECTOR, "#pgBd > div.search > div.leftcol > div > ul > li.searchresult.band > div > div.heading > a")
LOCATOR_BANDCAMP_HOMELAND = (By.CSS_SELECTOR, "#band-name-location > span.location.secondaryText")