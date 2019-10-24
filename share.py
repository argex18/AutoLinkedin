from traceback import print_exc
from os import listdir, getcwd, path
from itertools import zip_longest

import pyautogui as gui
from selenium import webdriver
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def share(browser):
    images = [".jpg", ".gif", ".png", ".eps", ".raw", ".cr2", ".nef", ".orf", ".sr2"]
    videos = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
    documents = [".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wks", ".wps", ".wpd"]
    try:
        text = ""
        desc = ""
        if isinstance(browser, webdriver.Chrome):
            for content in listdir(getcwd() + "\\shares"):
                if path.isdir(getcwd() + "\\shares\\" + content):
                    continue

                for image, video, document in zip_longest(images, videos, documents):
                    if image != None and str(content).endswith(image):
                        WebDriverWait(browser, 30).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[@id="ember48"]/div/div[1]/button[2]'))
                        )
                        browser.find_element_by_xpath('//*[@id="ember48"]/div/div[1]/button[2]').click()
                    
                    if video != None and str(content).endswith(video):
                        WebDriverWait(browser, 30).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[@id="ember48"]/div/div[1]/button[3]'))
                        )
                        browser.find_element_by_xpath('//*[@id="ember48"]/div/div[1]/button[3]').click()
                    
                    if document != None and str(content).endswith(document):
                        WebDriverWait(browser, 30).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[@id="ember48"]/div/div[1]/button[4]'))
                        )
                        browser.find_element_by_xpath('//*[@id="ember48"]/div/div[1]/button[4]').click()

                        WebDriverWait(browser, 30).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="ember1102"]/label/span'))
                        )
                        browser.find_element_by_xpath('//*[@id="ember1102"]/label/span').click()

                gui.click(271, 529)
                gui.typewrite(getcwd() + "\\shares\\" + content)
                gui.typewrite(["enter"])

                for alt in listdir(getcwd() + "\\shares\\alts"):
                    if alt.endswith(".txt") and alt.replace(".txt", "") == content.split(".")[0]:
                        with open(getcwd() + "\\shares\\alts\\" + alt, "r") as f:
                            text = f.read()
                    
                for description in listdir(getcwd() + "\\shares\\descriptions"):
                    if alt.endswith(".txt") and alt.replace(".txt", "") == content.split(".")[0]:
                        with open(getcwd() + "\\shares\\descriptions\\" + description, "r") as f:
                            desc = f.read()

                if text != -1:
                    if len(text) <= 120:
                        WebDriverWait(browser, 30).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div/footer/button'))
                        )
                        browser.find_element_by_xpath('/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div/footer/button').click()

                        alt = browser.find_element_by_xpath('/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/form/div[1]/div/input')
                        alt.send_keys(text)

                        WebDriverWait(browser, 30).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/form/div[2]/button[2]'))
                        )
                        browser.find_element_by_xpath('/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/form/div[2]/button[2]').click()
                    else:
                        raise ValueError("The image alternative text must not go over 120 characters")
                else:
                    print("The content of the alt file for the " + share + " share is empty")

                WebDriverWait(browser, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div/footer/div/button[2]'))
                )
                browser.find_element_by_xpath('/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div/footer/div/button[2]').click()

                if desc != -1:
                    description = browser.find_element_by_xpath('/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div[1]/div[3]/div[1]/div/div[1]/p')
                    description.send_keys(desc)
                else:
                    print("The content of the description file for the " + share + " share is empty")
                    
                WebDriverWait(browser, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/button'))
                )
                browser.find_element_by_xpath('/html/body/div[6]/div[7]/div[4]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/button').click()
        else:
            raise TypeError(str(browser) + " is not a valid webdriver argument")
    except TypeError:
        print_exc()
    except common.exceptions.TimeoutException:
        print("Something went wrong during finding a clickable element")
        print_exc()
    except ValueError:
        print_exc()
    except common.exceptions.NoSuchElementException:
        print_exc()

if __name__ == "__main__":
    print("This script cannot be run directly")