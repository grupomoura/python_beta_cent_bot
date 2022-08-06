from lib2to3.pgen2.driver import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from ast import literal_eval
from TwitterSearch import *
from tkinter import END
import pandas as pd 
import selenium
import shutil
import numpy
import time
import os

# Selenium argumentos
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = Options()
#options.add_argument('headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument("disable-infobars")
options.add_argument("disable-gpu")
options.add_argument("log-level=3")
options.add_argument(r"user-data-dir={}".format(profile))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Variáveis diversas
# friends = literal_eval(config['DATABASE']['friends_list'])
# keywords = literal_eval(config['DATABASE']['palavras'])
# nft_wallet = config['APP']['nft_wallet']
# twitter_login = config['TWITTER']['twitter_login']
# followings = []
# twitters = {}
# counts = 0

def delete_cache_driver():
    Cache = r"profile\wpp\Default\Cache"
    Code_Cache = r"profile\wpp\Default\Code Cache"
    try:
        shutil.rmtree(Cache)
        shutil.rmtree(Code_Cache)
    except OSError as e:
        print(e)
    else:
        print("Cache chrome liberado com successo")

def selectRandom(names, num=5):
  return numpy.random.choice(names, num, False)

def get_links():
    driver.get('https://beta.cent.co/cent/+4fthaj')
    time.sleep(4)
    links = driver.find_elements(By.CSS_SELECTOR, 'a')
    links_urls= []
    for link in links:
        link = link.get_attribute('href')
        if link:
            if not 'beta' in link and 'cent.co' in link and not '/legal/' in link:
                links_urls.append(link)
    print(links_urls)    
    return links_urls

    
def nft_verify_collect():
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    try:
        collect_buttons = driver.find_elements(By.TAG_NAME, "button") #Like
        try:
            subscribe_button = driver.find_element(By.XPATH, value=('//*[@id="root"]/div/div/div[2]/button/div'))
        except:
            pass
        count_collect = 0
        if collect_buttons:
            for button in collect_buttons:
                try:
                    if button.accessible_name == 'Collect' or button.text == 'Collect': 
                        try:
                            if subscribe_button:
                                subscribe_button.click()
                                time.sleep(4)
                        except:
                            pass
                        button.click() #Like
                        time.sleep(4)
                        count_collect+=1
                except:
                    pass
        if count_collect > 0:
            buttons_buy = driver.find_elements(by=By.CLASS_NAME, value=('purchase-nft-modal'))
            for button in buttons_buy:
                if 'price' in button.text.lower() or 'service fee' in button.text.lower():
                    count_collect-=1
        return count_collect
    except:
        return 0

def main():
    num_twitters_run = 0
    posts = 0

    while True:
        links_urls = get_links()
        
        if links_urls:
            for i, link in enumerate(links_urls):
                print('#'*80)
                url = link
                print(f'Acessando link {i+1}: {url}')                    
                driver.get(url)
                time.sleep(3)
                try:
                    count_clicks = nft_verify_collect()   
                    posts += count_clicks
                    if posts > 0:
                        print(f'{posts} NFTs coletadas com sucesso!')
                except:
                    time.sleep(20)
            print('\nColeta executada com sucesso!')
            delete_cache_driver()
            print('\nAguardando próxima coleta!')
            time.sleep(3600) # Uma hora 
        else:
            time.sleep(60)
main()

# button_retwitt = driver.find_elements(by=By.XPATH, value=('//*[@data-testid="retweet"]')) 
# posts_index = driver.find_elements(by=By.XPATH, value=('//*[@data-testid="retweetConfirm"]')) 
# button_like = driver.find_elements(by=By.XPATH, value=('//*[@aria-label="Curtir"]')) 
driver.find_elements(by=By.CLASS_NAME, value=('//*[@data-testid="tweetButtonInline"]')) 

"""
@alanz1k 
@Punk278 
@PatrickNJ16
@bluenft
@RaffaXdy
@Bruninho0721
@Robson25404655
@Daniel69248750
@letsboracrypto
@Oriebir_1234
@gicabrother
@Raphael_RT5
@deiltonFM
@emer_jenb9
"""

# 0x5565CD8a2ea7dc42427Ba99F6b261D2985005CcB
# driver.find_element(by=By.XPATH, value=('//*[@aria-label="Responder"]')).click()

#pyinstaller --onefile beta_cent_bot.py