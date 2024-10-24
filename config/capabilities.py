# Options 설정
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='R9PT507HHXA',
    appPackage='in.payhere.dev',
    appActivity='in.payhere.MainActivity',
    dontStopAppOnReset = True,#앱 현상태 유지한 상태에서 최초 실행
    noReset=True,#앱 시작하지 않음
)