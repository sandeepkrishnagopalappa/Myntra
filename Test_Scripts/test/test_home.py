""" This is the page where all the functions of TV page Apis called from here """
import pytest

@pytest.mark.usefixtures("instance")
class TestDemo1:
    """ This class uses all the fixtures """
    def test_home(self):
        """ From this method only we call all the functions """
        page_title = self.cart.men_button_hover()
        assert self.conf.expected_title == page_title, "The Home page title didnt match "
        self.cart.click_casual_shoe()
        self.cart.puma_checkbox()
        self.cart.price_checkbox()
        try:
            self.cart.click_casual_shoe()
        except Exception as e:
            print(e)
        names=self.cart.shoe_name()
        assert names == True ,"All shoes are not  PUMA brand  "
        self.cart.sort_hover()
        self.cart.high_to_low()
        self.cart.select_shoe()
        self.cart.window_switch()
        title_=self.cart.select_size()
        assert self.conf.expected_cart_page_title == title_, "The Cart  page title didnt match "
        self.cart.add_to_cart()
        try:
            self.cart.add_to_cart()
        except Exception as e:
            print(e)
        self.cart.go_to_cart()



