"""module for all generic methods"""
from selenium.webdriver.common.action_chains import ActionChains


class GenericMethod:
    """click, text, radio button, check box"""
    @staticmethod
    def click_on_element(driver,locator):
        """clicking element"""
        locator_type,locator_value=locator
        driver.find_element(locator_type,locator_value).click()

    @staticmethod
    def get_elements(driver,locator):
        """ Getting  element """
        locator_type,locator_value=locator
        return driver.find_elements(locator_type,locator_value)

    @staticmethod
    def get_page_title(driver):
        """title"""
        return driver.title

    @staticmethod
    def hover(driver,locator):
        """ Hovering """
        locator_type,locator_value=locator
        actions=ActionChains(driver)
        about=driver.find_element(locator_type,locator_value)
        actions.move_to_element(about).perform()

