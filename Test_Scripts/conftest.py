""" This is file where we create driver instance and all the  instances """
from Test_Scripts import *
@pytest.fixture(params=['CHROME','InternetExpo'],scope = 'session',autouse=True)
def driver_init(request):
    """ Creating driver instance """
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    if request.param =='CHROME':
        driver = webdriver.Chrome(Config.executable_path,options=options)
    if request.param =='InternetExpo':
        driver = webdriver.Ie(Config.executable_path_ie)
    request.session.driver = driver
    request.session.driver.implicitly_wait(15)
    yield
    request.session.driver.quit()

@pytest.fixture(scope = 'session',autouse=True)
def url_init(request,driver_init):
    """ Opening and closing the browser """
    request.session.driver.get(Config.url)
    request.session.driver.maximize_window()
    yield
    request.session.driver.quit()

@pytest.fixture(scope = 'class',autouse=True)
def instance(request,url_init):
    """ Creating an instance for class TvPom """
    request.cls.conf = Config()
    request.cls.cart = CartPage(request.session.driver)
