from appium.webdriver.common.mobileby import MobileBy as By

locators = {
    'hamburger button': (By.ACCESSIBILITY_ID, 'Change the current view'),
    # TODO: talk to developer about updating app to use id or accessibility id
    'collapse projects button': (By.XPATH, '(//android.widget.ImageView[@content-desc="Expand/collapse"])[1]'),
    'inbox button': (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                               'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                               'android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/'
                               'android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/'
                               'android.widget.TextView'),
    'project name view': (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'),
    'add task button': (By.ID, 'com.todoist:id/fab'),
    'save task': (By.ID, 'android:id/button1'),
    'task message field': (By.ID, 'android:id/message'),
    'task message view': (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'),
    'toolbar': (By.ID, 'com.todoist:id/toolbar'),
    'complete task button': (By.ACCESSIBILITY_ID, 'Complete')
}

