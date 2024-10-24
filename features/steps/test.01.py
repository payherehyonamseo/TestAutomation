import time
from behave import given, when, then
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from config.capabilities import capabilities

# Appium 서버 URL 설정
appium_server_url = 'http://0.0.0.0:4723/wd/hub'

@given('the app is launched')
def step_impl(context):
    # Appium 드라이버 초기화 (capabilities 명시적으로 전달)
    options = UiAutomator2Options().load_capabilities(capabilities)
    context.driver = webdriver.Remote(appium_server_url, options=options)
    # 앱이 로드될 때까지 딜레이
    time.sleep(15)


@when('I click the product management button')
def step_impl(context):
    # 상품 관리 버튼 클릭 전에 딜레이
    time.sleep(2)

    # 상품 관리 버튼 클릭
    context.driver.find_element(By.XPATH, "//*[@text='상품 관리']").click()


@then('I should see the WebView and click it')
def step_impl(context):
    # WebView 나타날 때까지 대기 후, 클릭 전에 딜레이 추가
    time.sleep(2)

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="android.webkit.WebView"]'))
    )

    # WebView 클릭
    context.driver.find_element(By.XPATH, "//*[@class='android.webkit.WebView']").click()


# 테스트가 끝난 후 리소스 정리
def after_scenario(context, scenario):
    # 드라이버 종료 전 딜레이
    time.sleep(2)

    context.driver.quit()