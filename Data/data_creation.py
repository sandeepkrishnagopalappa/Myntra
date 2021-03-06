from Data import *
from config import Config

data = {
    "men_button_hover":{"locator_type":"xpath",
                        "locator_value":"//div[@class='desktop-navLink']//a[text()='Men']"},
    "casual_shoe":{"locator_type":"xpath",
                    "locator_value":"//a[@href='/men-casual-shoes']"},
    "puma_checkbox":{"locator_type":"xpath",
                    "locator_value":"//ul[@class='brand-list']//label[text()='Puma']//div"},
    "price_checkbox":{"locator_type":"xpath",
                    "locator_value":"//li//label[text()='Rs. 6615 to Rs. 9308']//div"},
    "sort_hover":{"locator_type": "xpath",
                  "locator_value":"//div[@class='sort-sortBy']"},
    "price_high_to_low":{"locator_type":"xpath",
                        "locator_value":"//label[@class='sort-label ' and text()='Price: High to Low']"},
    "select_shoe":{"locator_type":"xpath",
                  "locator_value":"//img[@title='Puma Unisex White & Black Colourblocked Sneakers']"},
    "select_size":{"locator_type":"xpath",
                 "locator_value":"//p[text()='10']"},
    "add_to_cart":{"locator_type":"xpath",
                 "locator_value":"//div[text()='ADD TO BAG']"},
    "go_to_cart":{"locator_type":"xpath",
                "locator_value":"//span[text()='Bag']"},
    "shoe_price":{"locator_type":"xpath",
                "locator_value":"//div[@class='product-productMetaInfo']//div[@class='product-price']"},
    "shoe_name": {"locator_type": "xpath",
                   "locator_value": "//a//div[@class='product-productMetaInfo']//h3"},
    "text_of_shoe":{"locator_type": "xpath",
                   "locator_value": "//div[@class='itemContainer-base-details']//a"}
}

fileobj = open(Config.OBJECT_JSON,'w+')
json.dump(data, fileobj, indent=4)
fileobj.close()