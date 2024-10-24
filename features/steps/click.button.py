from behave import given, when, then
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

appium_server_url = 'http://0.0.0.0:4723/wd/hub'
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='R9PT507HHXA',
    appPackage='in.payhere.dev',
    appActivity='in.payhere.MainActivity',
    language='en',
    locale='US',
    noReset=True,
)

@given('I have launched the app')
def step_impl(context):
    options = UiAutomator2Options().load_capabilities(capabilities)
    context.driver = webdriver.Remote(appium_server_url, options=options)

@when('I click the permission button')
def step_impl(context):
    by = AppiumBy.ID
    value = "your_permission_button_id"  # 실제 권한 버튼의 ID를 입력
    allow_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((by, value))
    )
    allow_button.click()

@then('I should see the sound button')
def step_impl(context):
    el = context.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="판매"]')
    el.click()