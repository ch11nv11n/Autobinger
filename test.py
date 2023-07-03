import settings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# chrome libs
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
import re
import requests
import random
import json
import smtplib,ssl

points_per_search = 5

def main(): 
    driver = browser_select('chrome')
    account_login(driver)
    attempts = 0
    max_attempts = 3  # You can change this to whatever limit is appropriate
    while attempts < max_attempts:    
        pc_current_score, pc_total_score, mobile_current_score, mobile_total_score, edge_current_score, edge_total_score = get_score(driver)
        print("PC Search Score: ", pc_current_score)
        print("Mobile Search Score: ", mobile_current_score)
        print("Microsoft Edge Bonus Score: ", edge_current_score)
        pc_searches_needed = int((pc_total_score - pc_current_score) / points_per_search)
        mobile_searches_neeeded = int((mobile_total_score - mobile_current_score) / points_per_search)
        edge_searches_needed = int((edge_total_score - edge_current_score) / points_per_search)
        if pc_searches_needed == 0 and mobile_searches_neeeded == 0 and edge_searches_needed == 0:
            print("All scores are 0, breaking the loop...")
            break   
        check_scores(driver, pc_searches_needed, mobile_searches_neeeded, edge_searches_needed)
        print("Rechecking scores after performing searches...")
        print('All searches complete')
        attempts += 1
    if attempts == max_attempts:
        print(f"Reached maximum attempts ({max_attempts}), scores did not reach 0.")       
    input('Complete')
    

def browser_select(browser):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    if browser == 'chrome':
        # For chrome, we don't need to set anything.
        pass
    elif browser == 'firefoxMb':
        options.add_argument('user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/114.0 Mobile/15E148 Safari/605.1.15')
    elif browser == 'edge':
        options.add_argument('user-agent=Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edge/40.15254.603')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver


def fill_form(driver,css_selector,key):
    form_element = driver.find_element(By.CSS_SELECTOR, css_selector)
    if form_element:
        form_element.clear()
        form_element.send_keys(key)
        form_element.send_keys(Keys.RETURN)
        return True  
    return False


def check_login_success(driver):  
    success_indicator = driver.find_element(By.CSS_SELECTOR, 'div.identity')
    return success_indicator


def account_login(driver):
    while True:
        try:
            driver.get('https://login.live.com/')   
            if fill_form(driver,'[name="loginfmt"]',settings.USERNAME):
                time.sleep(5)
            if fill_form(driver,'[name="passwd"]',settings.PASSWORD):
                time.sleep(5)
            if check_login_success(driver):
                print('Login Successful')
                break
        except Exception as e:
            print(f'An error occurred: {e}')
            time.sleep(5)


def get_score(driver):
    while True:
        try:
            driver.get('https://rewards.microsoft.com/pointsbreakdown')
            point_types = driver.find_elements(By.CSS_SELECTOR, '[class="cardContainer"]')
            for i in point_types:
                # search for the pattern after "PC search"
                match_pc = re.search(r'PC search\n(\d+ / \d+)', i.text)
                if match_pc:
                    pc_search_score = match_pc.group(1)
                    pcCurrentScore, pcTotalScore = map(int, pc_search_score.split('/'))                   
                # search for the pattern after "Mobile search"
                match_mobile = re.search(r'Mobile search\n(\d+ / \d+)', i.text)
                if match_mobile:
                    mobile_search_score = match_mobile.group(1)
                    mobileCurrentScore, mobileTotalScore = map(int, mobile_search_score.split('/'))                    
                # search for the pattern after "Microsoft Edge bonus"
                match_edge = re.search(r'Microsoft Edge bonus\n(\d+ / \d+)', i.text)
                if match_edge:
                    microsoft_edge_bonus_score = match_edge.group(1)
                    edgeCurrentScore, edgeTotalScore = map(int, microsoft_edge_bonus_score.split('/'))
                return pcCurrentScore, pcTotalScore, mobileCurrentScore, mobileTotalScore, edgeCurrentScore, edgeTotalScore                
        except Exception as e:
            print(f'An error occurred: {e}')
            time.sleep(5)
    

def check_scores(driver, pc_searchs_needed, mobile_searchs_needed, edge_searches_needed):
    while True:
        if pc_searchs_needed == 0 and mobile_searchs_needed == 0 and edge_searches_needed == 0:
            print("All values are confirmed to be 0")
            driver.close()
            return
        else:
            print("Some scores are not zero, performing searches...")
            if pc_searchs_needed != 0:
                perform_search(driver,pc_searchs_needed)              
            if mobile_searchs_needed != 0:
                driver = browser_select('firefoxMb')
                account_login(driver)
                perform_search(driver,mobile_searchs_needed)               
            if edge_searches_needed != 0:
                driver = browser_select('edge')
                account_login(driver)
                perform_search(driver,edge_searches_needed)
            return            


def searchTermList(num_of_searches):
    rand_word_list_url = 'https://www.randomlists.com/data/words.json'
    r = requests.get(rand_word_list_url)
    word_list = random.sample(json.loads(r.text)['data'], num_of_searches)
    return word_list


def perform_search(driver,num_of_searches):
    time.sleep(6)
    for num,word in enumerate(searchTermList(num_of_searches)):
        print('{0}. URL : {1}'.format(str(num + 1), settings.BINGURL + word))
        try:
            driver.get(settings.BINGURL + word)
        except Exception as e1:
            print(e1)       
        time.sleep(3)


def send_email():
    smtp_port = settings.SMTP_PORT
    smtp_server = settings.SMTP_SERVER
    email_from = settings.FROM_ADDR
    email_to = settings.TO_ADDR
    email_password = settings.EMAIL_PASSWORD
    simple_email_context = ssl._create_default_https_context()
    message = 'Subject: {}\n\n{}'.format('AutoBinger Complete', 'All Bing searches complete')
    try:
        print('connecting to smtp server...')
        TIE_server = smtplib.SMTP(smtp_server,smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(email_from,email_password)
        print('connected to smtp server')
        print(f'sending email to {email_to}')
        TIE_server.sendmail(email_from,email_to,message)
        print(f'email successfully sent to {email_to}')   
    except Exception as e:
        print(e)
    finally:
        TIE_server.quit()


if __name__ == '__main__':
    main()