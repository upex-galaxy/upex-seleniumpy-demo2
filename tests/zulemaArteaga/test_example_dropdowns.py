from tests.testbase import *
import random


class TestDropdownsAsExample:

    def test_dropdowns(self, setup: Test):
        web, get = setup
        web.get('https://demoqa.com/select-menu')

        def select_dropdown_random_option():
            options = get.byXpaths(
                '//*[starts-with(@id, "react-select")][contains(@id, "option")]')
            count = len(options)
            random_index = random.randint(0, count - 1)
            given_element = options[random_index]
            given_text = given_element.text

            given_element.click()
            return given_text

        get.contains('Select Option').click()
        actual_value = select_dropdown_random_option()

        def select_dropdown_option(option_value: str):
            dropdown_option = get.byXpath(
                f'//*[starts-with(@id, "react-select")][contains(@id, "option")][contains(text(), "{option_value}")]')
            dropdown_option.click()

        get.contains(actual_value).click()
        select_dropdown_option('root')
