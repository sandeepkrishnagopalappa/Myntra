""" Reading the json file """
import json

class ReadJson:
    """class to read locators from json"""
    @staticmethod
    def read_locators(filelocation):
        """loading the data from json file"""
        with open(filelocation) as file:
            json_obj = json.load(file)
            dict_ = {}
            for key, value in json_obj.items():
                dict_[key] = (value['locator_type'], value['locator_value'])
        return dict_
