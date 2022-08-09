from appium import webdriver


class OpenApp():
    
    # App Capabilities
    desired_caps = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android Emulator',
        app=(r'PATH_TO_APK'),
        appWaitPackage= "com.supercook.app",
        appWaitActivity= "com.supercook.app.MainActivity",
        # newCommandTimeout= "5000"
    )
    
    # Launch the app with the capabilities applied
    def get_driver(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        return driver
    
