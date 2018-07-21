from appium.webdriver.common.mobileby import MobileBy as By

locators = {
    'email button': (By.ID, 'com.todoist:id/btn_welcome_continue_with_email'),
    'email field': (By.ID, 'com.todoist:id/email_exists_input'),
    'continue with email button': (By.ID, 'com.todoist:id/btn_welcome_continue_with_email'),
    'continue button': (By.ID, 'com.todoist:id/btn_continue_with_email'),
    'password field': (By.ID, 'com.todoist:id/log_in_password'),
    'login button': (By.ID, 'com.todoist:id/btn_log_in'),
    'toolbar': (By.ID, 'com.todoist:id/toolbar')
}
