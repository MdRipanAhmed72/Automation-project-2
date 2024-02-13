import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def Login_valid_function_test():
    # STEP1 FOR THE TEST
    driver = webdriver.Firefox ()
    driver.maximize_window ()

    driver.get ( "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" )
    time.sleep ( 20 )

    User_name = driver.find_element ( By.NAME , "username" )
    User_name_filed_status  = User_name.is_enabled()

    if User_name_filed_status:
        print(User_name_filed_status)
        User_name.clear()
        User_name.send_keys ( "Admin" )

    else:
        ("user name incorrect")

    User_pasword = driver.find_element ( By.NAME , "password" )
    user_pasword_field = User_pasword.is_enabled()

    if user_pasword_field:
        User_pasword.clear()
        User_pasword.send_keys ( "admin123" )
    else:
        print("wornig password")

        Login_button = driver.find_element ( By.CSS_SELECTOR , ".orangehrm-login-button" )
        Login_button.click ()
    time.sleep ( 20 )

    expectexd_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    actual_url = driver.current_url

    if expectexd_url == actual_url:
        print("Login successfully")
    else:
        print("login failed")

    driver.close ()




def test_fast_one_invliad_issue():
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(20)

    User_name = driver.find_element(By.NAME, "username")
    User_name.send_keys("Admin12")

    User_pasword = driver.find_element(By.NAME, "password")
    User_pasword.send_keys("admin1234")

    Login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    Login_button.click()
    time.sleep(5)
    # driver.close ()
    error_massage = driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text")
    actual_error_massage_text = error_massage.text

    expected_error_massage = "Invalid credentials"

    if expected_error_massage == actual_error_massage_text:
        print("lgin failed.error_massage:" +expected_error_massage)

    else:
        print("did not get:"+ expected_error_massage)

    driver.close()

#test_fast_one_invliad_issue()
Login_valid_function_test()
