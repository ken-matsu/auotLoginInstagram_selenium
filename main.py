from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url_base = "https://www.instagram.com/"
LOGIN_ID = ""
PASSWORD = ""

def get_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    
    return driver

def do_login(driver):
    login_url = url_base + LOGIN_ID +"/login/"
    driver.get(login_url)

    elem_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located_by_name( "username"))
    
    try:
        # パスワードのinput要素
        elem_password = driver.find_element_by_name("password")
    
        if elem_id and elem_password:
            # ログインID入力
            elem_id.send_keys(LOGIN_ID)
          
            # パスワード入力
            elem_password.send_keys(PASSWORD)
              
      
            # ログインボタンクリック
            elem_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located_by_((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
             
            actions = ActionChains(driver)
            actions.move_to_element(elem_btn)
            actions.click(elem_btn)
            actions.perform()
 
            # 適当（3秒間待つように対応しています）
            time.sleep(3)
 
            # 遷移
            # 遷移後のURLでログイン可否をチェック
            perform_url = driver.current_url
              
            if perform_url.find(login_url) == -1:
                # ログイン成功
                return True
            else:
                # ログイン失敗
                return False
               
        else:
            return False
    except:
        return False 
 
if __name__ == "__main__":
       
    # Driver
    driver = get_driver()
    # ログイン
    login_flg = do_login(driver)
      
    print(login_flg)
    driver.quit()