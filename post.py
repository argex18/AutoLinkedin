from traceback import print_exc
from os import listdir, getcwd

from selenium import webdriver
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def post(browser):
    try:
        if isinstance(browser, webdriver.Chrome):
            for post in listdir(getcwd() + "\\posts"):
                if post.endswith(".txt"):
                    with open(getcwd() + "\\posts\\" + post, "r") as f:
                        content = f.read()
                        WebDriverWait(browser, 30).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div/div[1]/button[1]'))
                        )
                        browser.find_element_by_xpath('/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div/div[1]/button[1]').click()

                        text_area = browser.find_element_by_xpath('/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/p')
                        
                        if content != -1:
                            text_area.send_keys(content)
                            WebDriverWait(browser, 30).until(
                                EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/button/span'))
                            )
                            browser.find_element_by_xpath('/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/button/span').click()
                        else:
                            print("The file " + post + " is empty")
        else:
            raise TypeError(str(browser) + " is not a valid webdriver argument")
    except TypeError:
        print_exc()
    except common.exceptions.TimeoutException:
        print("Something went wrong during finding a clickable element")
        print_exc()
    except common.exceptions.NoSuchElementException:
        print_exc()
        
if __name__ == "__main__":
    print("This script cannot be run directly")