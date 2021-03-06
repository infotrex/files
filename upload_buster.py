import tkinter
import subprocess
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from turtle import width
from PIL import ImageTk, Image
import urllib.request
from io import BytesIO
import os
import io
import sys
import pickle
import time
from decimal import *
import webbrowser
# from click import command
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import timedelta  
import dateutil.relativedelta
from datetime import timedelta, date
import locale
import json 
import ssl
import random
from fake_useragent import UserAgent

ssl._create_default_https_context = ssl._create_unverified_context

#check local date format
locale.setlocale(locale.LC_ALL, '')
lastdate = date(date.today().year, 12, 31)

root = Tk()
root.geometry('750x800')
root.resizable(False, False)
root.title("NFTs Upload to OpenSea v1.9.1")
  
input_save_list = ["NFTs folder :", 0, 0, 0, 0, 0, 0, 0, 0, 0]
main_directory = os.path.join(sys.path[0])


def supportURL():
    webbrowser.open_new("https://www.infotrex.net/opensea/support.asp?r=app")

def coffeeURL():
    webbrowser.open_new("https://github.com/infotrex/bulk-upload-to-opensea/#thanks")


class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        #self.image = tk.PhotoImage(data=base64.encodebytes(raw_data))
        image = Image.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image
imageurl = "https://www.infotrex.net/opensea/header.png"
img = WebImage(imageurl).get()
imagelab = tk.Label(root, image=img)
imagelab.grid(row=0, columnspan=2)
imagelab.bind("<Button-1>", lambda e:supportURL())

is_polygon = BooleanVar()
is_polygon.set(True)

is_listing = BooleanVar()
is_listing.set(True) 

is_numformat = BooleanVar()
is_numformat.set(False) 

is_unlockable = BooleanVar()
is_unlockable.set(False) 

is_sensitivecontent = BooleanVar()
is_sensitivecontent.set(False) 

def save_duration():
    duration_value.set(value=duration_value.get())
    # print(duration_value.get())

def save_unlockable():
    unlockable_value.set(value=unlockable_value.get())
    # print(duration_value.get())
    
def open_chrome_profile():
    subprocess.Popen(
        [
            "start",
            "chrome",
            "--remote-debugging-port=8989",
            "--user-data-dir=" + main_directory + "/chrome_profile",
            #"--user-data-dir=C:\\Users\\kelvin\\AppData\\Local\\Google\\Chrome\\User Data",
            # "--profile-directory=Default"

        ],
        shell=True,
    )


def save_file_path():
    return os.path.join(sys.path[0], "Save_gui.cloud") 


# ask for directory on clicking button, changes button name.
def upload_folder_input():
    global upload_path
    upload_path = filedialog.askdirectory()
    Name_change_img_folder_button(upload_path)

def Name_change_img_folder_button(upload_folder_input):
    upload_folder_input_button["text"] = upload_folder_input

def is_numeric(val):
	if str(val).isdigit():
		return True
	elif str(val).replace('.','',1).isdigit():
		return True
	else:
		return False

def check_exists_by_xpath(driver, xpath):
    try:
        # driver.find_element_by_xpath(xpath)
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

class InputField:
    def __init__(self, label, row_io, column_io, pos,  master=root):
        self.master = master
        self.input_field = Entry(self.master, width=60)
        self.input_field.grid(ipady=3)
        self.input_field.label = Label(master, text=label, anchor="w", width=20, height=1 )
        self.input_field.label.grid(row=row_io, column=column_io, padx=12, pady=2)
        self.input_field.grid(row=row_io, column=column_io + 1, padx=12, pady=2)
        
        try:
            with open(save_file_path(), "rb") as infile:
                new_dict = pickle.load(infile)
                self.insert_text(new_dict[pos])
        except FileNotFoundError:
            pass
        
    def insert_text(self, text):
        self.input_field.delete(0, "end")
        self.input_field.insert(0, text)

    def save_inputs(self, pos):
        #messagebox.showwarning("showwarning", "Warning")
        input_save_list.insert(pos, self.input_field.get())
        #print(self.input_field.get())
        with open(save_file_path(), "wb") as outfile:
            pickle.dump(input_save_list, outfile)
            
    def validate_inputs(self, maxlen, type, message):

        if type == 0 and (len(self.input_field.get()) == 0 or (self.input_field.get()).isdigit() != True or len(self.input_field.get()) > maxlen):
            messagebox.showwarning("showwarning", message)
                
        elif type == 1 and (len(self.input_field.get()) == 0 or is_numeric(self.input_field.get()) == False or len(self.input_field.get()) >= maxlen):
            messagebox.showwarning("showwarning", message)       
                
        elif type == 2 and ( len(self.input_field.get()) == 0 or len(self.input_field.get()) > maxlen):
            messagebox.showwarning("showwarning", message)
               
        else:
            return True     
        

###input objects###
collection_link_input = InputField("OpenSea Collection Link:", 2, 0, 1, 0)
start_num_input = InputField("Start Number:", 3, 0, 2, 0)
end_num_input = InputField("End Number:", 4, 0, 3, 0)
price = InputField("Default Price:", 5, 0, 4, 0)
title = InputField("Title:", 6, 0, 5, 0)
description = InputField("Description:", 7, 0, 6, 0)
file_format = InputField("NFT Image Format:", 8, 0, 7, 0)
external_link = InputField("External link:", 9, 0, 8, 0)
external_link = InputField("External link:", 9, 0, 8, 0)

def save():

    if len(start_num_input.input_field.get()) == 0 or len(end_num_input.input_field.get()) == 0 or (int(end_num_input.input_field.get()) < int(start_num_input.input_field.get())):
        #messagebox.showwarning("showwarning", "End number should greater than start number!")
        print ("true")
    elif len( start_num_input.input_field.get()) == 0 or len(end_num_input.input_field.get()) > 5 :
        #messagebox.showwarning("showwarning", "Start / end number range 0 - 99999")
        print ("true")
    else:
        collection_link_input.validate_inputs(200, 2, 'Collection link required')
        price.validate_inputs(100, 1, 'Price required')
        title.validate_inputs(100, 2, 'title required')
        description.validate_inputs(500, 2, 'description required')
        file_format.validate_inputs(100, 2, 'file format required - png, jpg, jpeg, gif')
        external_link.validate_inputs(300, 3, '')
     

    input_save_list.insert(0, upload_path)
    collection_link_input.save_inputs(1)
    start_num_input.save_inputs(2)
    end_num_input.save_inputs(3)
    price.save_inputs(4)
    title.save_inputs(5)
    description.save_inputs(6)
    file_format.save_inputs(7)
    external_link.save_inputs(8)


def main_program_loop():

    if len(end_num_input.input_field.get()) > 5 :
        messagebox.showwarning("showwarning", "Start / end number range 0 - 99999")
        sys.exit()

    project_path = main_directory
    file_path = upload_path
    collection_link = collection_link_input.input_field.get()
    start_num = int(start_num_input.input_field.get())
    end_num = int(end_num_input.input_field.get())
    loop_price = float(price.input_field.get())
    loop_title = title.input_field.get()
    loop_file_format = file_format.input_field.get()
    loop_external_link = str(external_link.input_field.get())
    loop_description = description.input_field.get()



    ##chromeoptions
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("debuggerAddress", "localhost:8989")
    # ua = UserAgent()
    # userAgent = ua.random
    # print(userAgent)
    # options.add_argument(f'user-agent={userAgent}')
    # driver = webdriver.Chrome(executable_path=project_path + "/chromedriver.exe",options=options)
    driver = webdriver.Chrome(service=Service(project_path + "/chromedriver.exe"), options=options )
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',options=options)
    wait = WebDriverWait(driver, 60)

    ###wait for methods
    def wait_css_selector(code):
        wait.until(
            ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code))
        )
        
    def wait_css_selectorTest(code):
        wait.until(
            ExpectedConditions.elementToBeClickable((By.CSS_SELECTOR, code))
        )    

    def wait_xpath(code):
        wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))
        
        
    def wait_xpath_clickable(code):
        wait.until(ExpectedConditions.element_to_be_clickable((By.XPATH, code)))
    
    def check_exists_by_tagname(tagname):
        try:
            # driver.find_element_by_tagname(tagname)
            driver.find_element(By.TAG_NAME, tagname)
        except NoSuchElementException:
            return False
        return True
            
    def delay(waiting_time=10):
            driver.implicitly_wait(waiting_time)

    def twocaptcha_bypass():
        delay()
        solved_info = WebDriverWait(driver, 30).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[@class='captcha-solver-info']" )))
        # solved_status = WebDriverWait(driver, 10).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[@class='captcha-solver-info']" ))).get_attribute("innerHTML")
        # print(str(solved_status))
        wait_xpath("//div[@class='captcha-solver']")
        captcha_solver_button = driver.find_element(By.XPATH, "//div[@class='captcha-solver']")
        driver.execute_script("arguments[0].click();", captcha_solver_button)
        time.sleep(sleeptime)
        WebDriverWait(driver, 60).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[@data-state='solving']" )))
        print("solving")
        WebDriverWait(driver, 300).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[@data-state='solved']")))
        print("solved")
    
    def buster_bypass():
        try:
            # capt_btn = WebDriverWait(driver, 50).until(ExpectedConditions.element_to_be_clickable((By.XPATH ,'//*[@id="recaptcha-audio-button"]')))
            wait_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[4]')
            capt_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[4]')
            # capt_btn.click()
            webdriver.ActionChains(driver).click(capt_btn).perform()
            time.sleep(sleeptime)
        except:
            capt_btn = WebDriverWait(driver, 20).until(ExpectedConditions.element_to_be_clickable((By.XPATH ,'//*[@id="solver-button"]')))
            # capt_btn = driver.find_element_by_xpath("//button[@id='solver-button']")
            driver.execute_script("arguments[0].click();", capt_btn)
            # webdriver.ActionChains(driver).click(capt_btn).perform()
            time.sleep(sleeptime)


    randomnumber1 = random.uniform(0.7, 0.99)
    randomnumber2 = random.uniform(2.11, 2.88)
    sleeptime = random.uniform(randomnumber1, randomnumber2)

    while end_num >= start_num:
        if is_numformat.get():
            start_numformat = f"{ start_num:04}"
        else:
             start_numformat = f"{ start_num:01}"

        print("Start creating NFT " +  loop_title + str(start_numformat))
        print('number ',  start_numformat)
        driver.get(collection_link)
        
        
        wait_xpath('//*[@id="media"]')
        imageUpload = driver.find_element(By.XPATH, '//*[@id="media"]')
        imagePath = os.path.abspath(file_path + "\\images\\" + str(start_numformat) + "." + loop_file_format)  # change folder here
        imageUpload.send_keys(imagePath)
        time.sleep(sleeptime)

        # if loop_file_format.lower() != "png" or loop_file_format.lower() != "jpg" or loop_file_format.lower() != "svg" or loop_file_format.lower() != "gif" :
        #     wait.until(ExpectedConditions.presence_of_element_located((By.NAME, 'preview')))
        #     imageUpload_preview = driver.find_element(By.NAME, 'preview')
        #     imageUpload_path = os.path.abspath(file_path + "\\images\\" + str(start_numformat) + ".png")  # change folder here
        #     imageUpload_preview.send_keys(imageUpload_path)
        #     time.sleep(sleeptime)

        wait_xpath('//*[@id="name"]')
        name = driver.find_element(By.XPATH, '//*[@id="name"]')
        name.send_keys(loop_title + str(start_numformat))  # +1000 for other folders #change name before "#"
        time.sleep(sleeptime)

        wait_xpath('//*[@id="external_link"]')
        ext_link = driver.find_element(By.XPATH, '//*[@id="external_link"]')
        ext_link.send_keys(loop_external_link)
        time.sleep(sleeptime)

        wait_xpath('//*[@id="description"]')
        desc = driver.find_element(By.XPATH, '//*[@id="description"]')
        desc.send_keys(loop_description)
        time.sleep(sleeptime)

        jsonFile = file_path + "/json/"+ str(start_numformat) + ".json"
        if os.path.isfile(jsonFile) and os.access(jsonFile, os.R_OK):
           
            #print(str(jsonMetaData))
            wait_css_selector("button[aria-label='Add properties']")
            properties = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add properties']")
            driver.execute_script("arguments[0].click();", properties)
            time.sleep(sleeptime)

            # checks if file exists
            jsonData = json.loads(open(file_path + "\\json\\"+ str(start_numformat) + ".json").read())
            
            if "attributes" in jsonData:
                jsonMetaData = jsonData['attributes']

                for key in jsonMetaData:
                    input1 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')
                    input2 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[2]/div/div/input')
                    #print(str(key['trait_type']))
                    #print(str(key['value']))
                    input1.send_keys(str(key['trait_type']))
                    input2.send_keys(str(key['value']))
                    addmore_button = driver.find_element(By.XPATH, '//button[text()="Add more"]')
                    driver.execute_script("arguments[0].click();", addmore_button)
                time.sleep(0.95)

                try:
                    save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
                    driver.execute_script("arguments[0].click();", save_button)
                    time.sleep(sleeptime)
                except:
                    driver.find_element(By.XPATH, '//button[text()="Save"]').click()
                    time.sleep(sleeptime)

            elif "properties" in jsonData:
                jsonMetaData = jsonData['properties']
                
                for key in jsonMetaData:
                    input1 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')
                    input2 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[2]/div/div/input')
                    #print(str(key['type']))
                    #print(str(key['name']))
                    input1.send_keys(str(key['type']))
                    input2.send_keys(str(key['name']))
                    addmore_button = driver.find_element(By.XPATH, '//button[text()="Add more"]')
                    driver.execute_script("arguments[0].click();", addmore_button)
                time.sleep(0.9)

                try:
                    save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
                    driver.execute_script("arguments[0].click();", save_button)
                    time.sleep(sleeptime)
                except:
                    driver.find_element(By.XPATH, '//button[text()="Save"]').click()
                    time.sleep(sleeptime)

            else:
                print("keys not found!") 

        if is_sensitivecontent.get():
            #Explicit & Sensitive toggle
            wait_xpath('//*[@id="explicit-content-toggle"]')
            toggle_sensivity = driver.find_element(By.XPATH,'//*[@id="explicit-content-toggle"]')
            # toggle_sensivity.location_once_scrolled_into_view
            driver.execute_script("return arguments[0].click();", toggle_sensivity)
            time.sleep(1.1)

        # Select Polygon blockchain if applicable
        wait_xpath('//*[@id="chain"]')
        default_blockchain = driver.find_element(By.ID, "chain").get_attribute("value")        
        print(default_blockchain)


        if is_polygon.get():
            
            if (default_blockchain != 'Polygon' and default_blockchain != 'Mumbai'):
                    
                blockchain_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/section/div/form/div[7]/div/div[2]')
                driver.execute_script("arguments[0].scrollIntoView();", blockchain_button)
                blockchain_button.click()
                polygon_button_location = '//span[normalize-space() = "Mumbai"]' and '//span[normalize-space() = "Polygon"]'
                wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, polygon_button_location)))
                polygon_button = driver.find_element(By.XPATH, polygon_button_location)
                polygon_button.click()

        else:
    
            if (default_blockchain != 'Ethereum' and default_blockchain != 'Rinkeby'):
                
                blockchain_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/section/div/form/div[7]/div/div[2]')
                driver.execute_script("arguments[0].scrollIntoView();", blockchain_button)
                blockchain_button.click()
                ethereum_button_location = '//span[normalize-space() = "Rinkeby"]' and '//span[normalize-space() = "Ethereum"]'
                wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, ethereum_button_location)))
                ethereum_button = driver.find_element(By.XPATH, ethereum_button_location)
                ethereum_button.click()

        
        create = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div/div[1]/span/button')
        driver.execute_script("arguments[0].click();", create)
        time.sleep(sleeptime)
        
        main_page = driver.current_window_handle
        
        if check_exists_by_xpath(driver, '//h4[text()="Almost done"]'):
            wait_xpath('//h4[text()="Almost done"]')
            captcha_element = driver.find_element(By.XPATH,'//h4[text()="Almost done"]')

            if check_exists_by_tagname('iframe'):

                iframes = driver.find_elements(By.TAG_NAME, "iframe")
                driver.switch_to.frame(iframes[0])

                try:
                    checkbox_button = WebDriverWait(driver, 30).until(ExpectedConditions.element_to_be_clickable((By.ID ,"recaptcha-anchor")))
                    checkbox_button.click()
                    # webdriver.ActionChains(driver).click(checkbox_button).perform()
                except:
                    pass
                
                driver.switch_to.default_content() 
                # driver.switch_to.frame(iframes[-1])

                # click on audio challenge
                WebDriverWait(driver, 30).until(ExpectedConditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge expires in two minutes']")))
                time.sleep(1)
                
                buster_bypass()

                try:
                
                    time.sleep(3)
                    audio_input = driver.find_element(By.ID, "audio-response").get_attribute('value')
                    if audio_input == "":
                        print("empty")
                        # WebDriverWait(driver, 30).until(ExpectedConditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge expires in two minutes']")))
                        # time.sleep(1)
                        try:
                        #     delay()
                        #     reset_buster_btn = driver.find_element(By.XPATH,"//*[@id='recaptcha-reload-button']")
                        #     driver.execute_script("arguments[0].click();", reset_buster_btn)
                        #     time.sleep(sleeptime)
                            print("reset")
                            
                        #     capt_button = WebDriverWait(driver, 20).until(ExpectedConditions.element_to_be_clickable((By.XPATH ,'//*[@id="solver-button"]')))
                        #     driver.execute_script("arguments[0].click();", capt_button)
                        #     # webdriver.ActionChains(driver).click(capt_btn).perform()
                        #     time.sleep(sleeptime)
                            
                        except:
                            pass
                        
                        

                        # twocaptcha_bypass()

                    else:
                        print("something")
                        
                except:
                    pass
                
                time.sleep(1)
                
                try:
                    # delay()
                    errorsTry = driver.find_element(By.CLASS_NAME,'rc-doscaptcha-header-text')
                    # driver.find_element('rc-doscaptcha-header-text')
        
                    reset_btn = driver.find_element(By.XPATH,"//*[@id='reset-button']")
                    driver.execute_script("arguments[0].click();", reset_btn)
                    time.sleep(sleeptime)
                    
                    # beep sound
                    # beep = lambda x: os.system("\a" * x)
                    # beep(1)

                    buster_bypass()

                
                except NoSuchElementException:
                    pass

       
                driver.switch_to.default_content()  
             

            else:
                print("captcha not found")
        else:
            print("no captcha")

        delay()
        if check_exists_by_xpath(driver, '//h1[text()="Oops, something went wrong"]'):
            sell_url = driver.current_url +"/sell";
            driver.get(sell_url)
            print("redirect to sell url")
            time.sleep(sleeptime)
        else:
            print("url")
        
            try:
                wait_xpath('/html/body/div[6]/div/div/div/div[2]/button/i')
                cross = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/button/i')
                cross.click()
                time.sleep(sleeptime)
            except:
                wait_xpath('/html/body/div[5]/div/div/div/div[2]/button/i')
                cross = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button/i')
                driver.execute_script("arguments[0].click();", cross)
                time.sleep(sleeptime)
    
        time.sleep(2)
            
        main_page = driver.current_window_handle

        if is_listing.get():

            if check_exists_by_xpath(driver, '//a[text()="Sell"]'):
                wait_xpath('//a[text()="Sell"]')
                sell = driver.find_element(By.XPATH, '//a[text()="Sell"]')
                driver.execute_script("arguments[0].click();", sell)
                time.sleep(sleeptime)
            else:    
                sell_url = driver.current_url +"/sell";
                driver.get(sell_url)
                print("sell button missing")
                time.sleep(sleeptime)

            if check_exists_by_xpath(driver, '//h1[text()="This page is lost."]'):
                print("This page is lost.")
      
                back_url = driver.back()
                driver.get(back_url)
                print("go back url")
                time.sleep(sleeptime)
            else:
                pass
                
                
            wait_css_selector("input[placeholder='Amount']")
            amount = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Amount']")
            amount.send_keys(str(loop_price))
            time.sleep(0.8)

            #duration
            duration_date = duration_value.get()

            #if duration_date != 30:
            # amount.send_keys(Keys.TAB * 8 + Keys.SPACE)
            amount.send_keys(Keys.TAB)
            # amount.send_keys(Keys.ENTER)
            time.sleep(2)

            wait_xpath('//*[@role="dialog"]/div[1]/div[1]/div/input')
            select_durationday = driver.find_element(By.XPATH, '//*[@role="dialog"]/div[1]/div[1]/div/input')
            select_durationday.click()
            if duration_date == 1 : 
                range_button_location = '//span[normalize-space() = "1 day"]'
            if duration_date == 3 : 
                range_button_location = '//span[normalize-space() = "3 days"]'
            if duration_date == 7 : 
                range_button_location = '//span[normalize-space() = "7 days"]'
            if duration_date == 30 : 
                range_button_location = '//span[normalize-space() = "1 month"]'    
            if duration_date == 90 : 
                range_button_location = '//span[normalize-space() = "3 months"]' 
            if duration_date == 180 : 
                range_button_location = '//span[normalize-space() = "6 months"]'     

            wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, range_button_location)))
            date_range_button = driver.find_element(By.XPATH, range_button_location)
            time.sleep(sleeptime)
            date_range_button.click()
            time.sleep(sleeptime)
            select_durationday.send_keys(Keys.ENTER)
            time.sleep(sleeptime)

            delay()
            wait_css_selector("button[type='submit']")
            listing = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            driver.execute_script("arguments[0].click();", listing)
            time.sleep(8)
            # time.sleep(sleeptime)
            
            if is_polygon.get():
                polygon_sign = WebDriverWait(driver, 10).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//button[text()='Sign']" )))
                driver.execute_script("arguments[0].click();", polygon_sign)
                time.sleep(sleeptime)

            for handle in driver.window_handles:
                if handle != main_page:
                    login_page = handle
                    #break
            
            driver.switch_to.window(login_page) 
               
            if is_polygon.get():
                try:
                    driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div[3]/div[1]").click()
                    time.sleep(0.7)
                except: 
                    wait_xpath("//div[@class='signature-request-message__scroll-button']")
                    polygonscrollsign = driver.find_element(By.XPATH, "//div[@class='signature-request-message__scroll-button']")
                    driver.execute_script("arguments[0].click();", polygonscrollsign)
                    time.sleep(0.7)

                try:
                    wait_xpath('//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]')
                    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]').click()
                    time.sleep(0.7)
                except:
                    wait_xpath('//button[text()="Sign"]')
                    metasign = driver.find_element(By.XPATH, '//button[text()="Sign"]')
                    driver.execute_script("arguments[0].click();", metasign)
                    time.sleep(0.7)
            else:
                try:
                    wait_xpath("//div[@class='signature-request-message__scroll-button']")
                    scrollsign = driver.find_element(By.XPATH, "//div[@class='signature-request-message__scroll-button']")
                    driver.execute_script("arguments[0].click();", scrollsign)
                    time.sleep(sleeptime)
                except: 
                    driver.find_element(By.XPATH, "//div[@class='signature-request-message__scroll-button']").click()
                    time.sleep(sleeptime)

                try:
                    wait_xpath('//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]')
                    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]').click()
                    time.sleep(sleeptime)
                except:
                    wait_xpath('//button[text()="Sign"]')
                    metasign = driver.find_element(By.XPATH, '//button[text()="Sign"]')
                    driver.execute_script("arguments[0].click();", metasign)
                    time.sleep(sleeptime)

  
        #change control to main page
        driver.switch_to.window(main_page)
        time.sleep(sleeptime)

        start_num = start_num + 1
        print('NFT creation completed!')
        time.sleep(sleeptime)
    
    driver.get("https://www.opensea.io")
    


unlockable_value = IntVar()
unlockable_value.set(value=180)
unlockable_content_frame = Frame(root, padx=0, pady=1)
unlockable_content_frame.grid(row=11, column=1)
unlockable_content_frame.label = Label(root, text="Unlockable Content:", anchor="nw", width=20, height=5 )
tk.Checkbutton(unlockable_content_frame, text='Yes', var=is_unlockable,  width=58, anchor="w", command=save_unlockable).grid(row=0, column=1)
tk.Text(unlockable_content_frame, width=48, height=3).grid(row=1, column=1, columnspan=2,pady=10)
unlockable_content_frame.label.grid(row=11, column=0, padx=12, pady=2)

duration_value = IntVar()
duration_value.set(value=180)
duration_date = Frame(root, padx=0, pady=1)
duration_date.grid(row=15, column=1, sticky=(N, W, E, S))
tk.Radiobutton(duration_date, text='1 day', variable=duration_value, value=1, anchor="w", command=save_duration, width=6,).grid(row=0, column=1)
tk.Radiobutton(duration_date, text="3 days", variable=duration_value, value=3, anchor="w", command=save_duration, width=6, ).grid(row=0, column=2)
tk.Radiobutton(duration_date, text="7 days", variable=duration_value, value=7, anchor="w", command=save_duration, width=6,).grid(row=0, column=3)
tk.Radiobutton(duration_date, text="30 days", variable=duration_value, value=30, anchor="w", command=save_duration, width=7,).grid(row=0, column=4)
tk.Radiobutton(duration_date, text="90 days", variable=duration_value, value=90, anchor="w",command=save_duration,  width=7,).grid(row=0,  column=5)
tk.Radiobutton(duration_date, text="180 days", variable=duration_value, value=180, anchor="w", command=save_duration, width=7).grid(row=0, column=6)
duration_date.label = Label(root, text="Duration:", anchor="nw", width=20, height=2 )
duration_date.label.grid(row=15, column=0, padx=12, pady=0)

isSensitive = tkinter.Checkbutton(root, text='Sensitive Content', var=is_sensitivecontent,   width=49, anchor="w")
isSensitive.grid(row=17, column=1)
isCreate = tkinter.Checkbutton(root, text='Complete Listing', var=is_listing, width=49, anchor="w")
isCreate.grid(row=19, column=1)
isPolygon = tkinter.Checkbutton(root, text='Polygon Blockchain (Auto switch)',  var=is_polygon, width=49, anchor="w")
isPolygon.grid(row=20, column=1)
upload_folder_input_button = tkinter.Button(root, width=50, height=1,  text="Add NFTs Upload Folder", command=upload_folder_input)
upload_folder_input_button.grid(row=21, column=1, padx=2)
open_browser = tkinter.Button(root, width=50, height=1,  text="Open Chrome Browser", command=open_chrome_profile)
open_browser.grid(row=23, column=1, pady=2)
button_save = tkinter.Button(root, width=50, height=1,  text="Save This Form", command=save) 
button_save.grid(row=22, column=1, pady=2)
button_start = tkinter.Button(root, width=44, height=2, bg="green", fg="white", text="Start", command=main_program_loop)
button_start['font'] = font.Font(size=10, weight='bold')
button_start.grid(row=25, column=1, pady=2)
# footer = tkinter.Button(root, height=3, width=60, text='Do you you want to show support? \n Now you have the chance to buy me a coffee. Thank you.',  command=coffeeURL, relief=GROOVE  )
# footer.grid(row=31, columnspan=2, padx=31, pady=31)

try:
    with open(save_file_path(), "rb") as infile:
        new_dict = pickle.load(infile)
        global upload_path
        Name_change_img_folder_button(new_dict[0])
        upload_path = new_dict[0]
        print(new_dict[8])
except FileNotFoundError:
    pass
#####BUTTON ZONE END#######
root.mainloop()
