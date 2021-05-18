from Pom import *

class CartPage(HomePage):
    """ This is the class of Tv page  """
    def __init__(self,driver):
        self.driver = driver
        self.variable1 = ReadJson.read_locators(Config.OBJECT_JSON)
        self.ObjectGen = GenericMethod()

    def select_size(self):
        """ select size """
        self.ObjectGen.hover(self.driver, self.variable1["select_size"])
        return self.ObjectGen.get_page_title(self.driver)

    def add_to_cart(self):
        """ Clicking on add to cart """
        self.ObjectGen.click_on_element(self.driver, self.variable1["add_to_cart"])

    def go_to_cart(self):
        """ Clicking on go to cart """
        self.ObjectGen.click_on_element(self.driver, self.variable1["go_to_cart"])
