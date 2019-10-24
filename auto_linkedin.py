from time import sleep
from traceback import print_exc

from selenium import webdriver
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from AutoLogin import lib
import post
import share

lib.PSEC = input("Insert the path of the your passwords file: ").replace("/", "\\")

def main():
    print("What do you want to do?:\n")
    print(" 1)Post all content in posts")
    print(" 2)Share all content in shares")
    print("\n:> ", end='')
    mode = int(input())
    browser = webdriver.Chrome(executable_path=input("Insert the path of the chrome driver for Selenium: ").replace("/", "\\"))
    try:
        if mode != 1 and mode != 2:
            raise ValueError("Invalid option selected")

        email = lib.find_data(lib.PSEC, "linkedin", lib.EPATTERN)
        password = lib.find_data(lib.PSEC, "linkedin", lib.PPATTERN)
        url = lib.find_field("linkedin", "url")
        email_xpath = lib.find_field("linkedin", "email_xpath")
        password_xpath = lib.find_field("linkedin", "password_xpath")
        submit_xpath = lib.find_field("linkedin", "submit_xpath_1")

        try:
            browser.get(url)
            browser.find_element_by_xpath(email_xpath).send_keys(email)
            browser.find_element_by_xpath(password_xpath).send_keys(password)

            if mode == 1:
                post.post(browser)
            else:
                share.share(browser)
        except common.exceptions.NoSuchElementException:
            print_exc()
        except common.exceptions.TimeoutException:
            print("Something went wrong during finding a clickable element")
            print_exc()
    except ValueError:
        print_exc()
    except:
        print_exc()
        sleep(30)
    finally:
        browser.quit()

if __name__ == "__main__":
    main()