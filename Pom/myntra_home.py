""" In this module we write all the Apis of Tv page """
from Pom import *

class HomePage:
    """ This is the class of Tv page  """
    def __init__(self,driver):
        self.driver = driver
        self.variable1 = ReadJson.read_locators(Config.OBJECT_JSON)
        self.ObjectGen = GenericMethod()

    def men_button_hover(self):
        """ men_button_hover """
        self.ObjectGen.hover(self.driver, self.variable1["men_button_hover"])
        return self.ObjectGen.get_page_title(self.driver)

    def click_casual_shoe(self):
        """ Clicking on casual shoe """
        self.ObjectGen.click_on_element(self.driver,self.variable1["casual_shoe"])

    def puma_checkbox(self):
        """ Clicking on puma checkbox """
        self.ObjectGen.click_on_element(self.driver,self.variable1["puma_checkbox"])

    def price_checkbox(self):
        """ Clicking on price checkbox """
        self.ObjectGen.click_on_element(self.driver,self.variable1["price_checkbox"])

    def select_shoe(self):
        """ Clicking on select shoe """
        self.ObjectGen.click_on_element(self.driver,self.variable1["select_shoe"])


    def shoe_name(self):
        """Getting the names of the shoe """
        name_text= self.ObjectGen.get_elements(self.driver, self.variable1["shoe_name"])
        name_=[i.text for i in name_text]
        count=0
        for i in name_:
            if i=='Puma':
                pass
            else:
                count+=1
        if count==0:
            return True


    def sort_hover(self):
        """ Sorting the elements """
        self.ObjectGen.click_on_element(self.driver, self.variable1["sort_hover"])

    def high_to_low(self):
        """clicking on high to low"""
        self.ObjectGen.click_on_element(self.driver, self.variable1["price_high_to_low"])

    def window_switch(self):
        """ handling window """
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[1])
        return self.ObjectGen.get_page_title(self.driver)


