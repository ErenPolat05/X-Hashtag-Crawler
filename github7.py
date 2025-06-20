from bSeleniumXinf import email , password , name
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Twitter:
    def __init__(self,email,password,name):
        self.browserprofile = webdriver.ChromeOptions()
        self.browserprofile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})       
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.browserprofile)
        self.email = email
        self.password = password
        self.name = name
    
    def SignIn(self):
        self.browser.get("https://x.com/i/flow/login")
        time.sleep(3)

        try:
                     
            emailinput = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']"))
            )
            emailinput.send_keys(self.email)
            emailinput.send_keys(Keys.ENTER)
            time.sleep(2)

          
            try:
                username_input = WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']"))
                )
                  
                if username_input.is_displayed():
                    print("username screen used")
                    username_input.send_keys(self.name)  
                    username_input.send_keys(Keys.ENTER)
                    time.sleep(2)
            except:
                print("username screen not used.")

        
            passwordinput = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
                )
            passwordinput.send_keys(self.password)
            passwordinput.send_keys(Keys.ENTER)
            time.sleep(3)
            print("Login Successful.")
        except Exception as error:
            print("An error occurred during login", error)

    
    def search(self,hashtag): 
        self.browser.get("https://x.com/home") 
        time.sleep(3)   

        self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]").click()
        time.sleep(2)



        searchinput = WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-testid='SearchBox_Search_Input']"))
        )
        searchinput.clear()
        searchinput.send_keys(hashtag)
        time.sleep(1)
        searchinput.send_keys(Keys.ENTER)
        time.sleep(3)


        results = []

        list = self.browser.find_elements(By.XPATH,"//div[@data-testid='tweet']")
        time.sleep(2)
        
        for i in list:
            results.append(i)

        loopcounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopcounter > 5:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopcounter += 1

            list = self.browser.find_elements(By.XPATH, "//article[@data-testid='tweet']")
            time.sleep(2)
            print("count :"+str(len(list)))

            for i in list:
                results.append(i.text)
        
        # count = 1
        # for item in results:
        #     print(f"{count} -- {item}")    # You Can Write On Terminal
        #     count += 1                     # <------  With This Code.
        #     print("*********")

        with open("tweetdepo.txt","w",encoding="utf-8") as file:
            for count, item in enumerate(results, 1):
             file.write(f"{count}--{item}\n")


twitter = Twitter(email,password,name)
twitter.SignIn()
twitter.search("python")
