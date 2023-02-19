from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#from con import write_data
import os
from tempfile import mkdtemp
from bs4 import BeautifulSoup
from typing import List
import time
import selenium
import contextlib
import json
import random
import undetected_chromedriver as uc


class instagram:
    def __init__(self, username: str, password: str, SLEEP_SECS: int) -> None:
        self.username = username
        self.password = password
        chrome_options = uc.ChromeOptions()
        chrome_options = Options()
        height = random.randint(400, 780)
        width = random.randint(800, 1120)
        user_agent = get_user_agent()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument(f'--user-agent={user_agent}')
        chrome_options.add_argument(f'window-size={width}x{height}')
        chrome_options.add_argument("--disable-popup-blocking")
        
        self.driver = uc.Chrome(options=chrome_options,
                                user_data_dir=mkdtemp())
        # self.main_url = "https://app.pictory.ai/login"
        # self.main_url = "https://app.pictory.ai/textinput"
        self.main_url= 'https://www.instagram.com/accounts/login/?source=auth_switcher'
        Download= "/home/rinku/Downloads/Wecanwriteatext.mp4"
        self.Upload = '/home/rinku/Downloads/Generated video.mp4'
        self.SLEEP_SECS = 1
        
    

    def login(self) -> None:
        print("Log IN......")
        self.driver.get(self.main_url)


        email = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        email.send_keys(self.username)
        time.sleep(self.SLEEP_SECS)

        password = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
        password.send_keys(self.password)
        time.sleep(self.SLEEP_SECS)

        btn = WebDriverWait(self.driver, 25).until(       
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))
        self.safe_click(btn)                             
        time.sleep(self.SLEEP_SECS)
        # time.sleep(600)
    def upload(self,Massage: str,path: str) -> None:
        # for i in range(20):
        # self.driver.get(self.main_url)
            # self.driver.get('https://www.instagram.com/rahul.b_5005/')
        
        # path="full path"+str(i)+"_.mp4" #for windows
        click_to_Create = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Create')]")))
        self.safe_click(click_to_Create)

        time.sleep(self.SLEEP_SECS)


        ###############################################################################################
        def drag_and_drop_file(drop_target, path)-> None:
            JS_DROP_FILE = """
                    var target = arguments[0],
                        offsetX = arguments[1],
                        offsetY = arguments[2],
                        document = target.ownerDocument || document,
                        window = document.defaultView || window;

                    var input = document.createElement('INPUT');
                    input.type = 'file';
                    input.onchange = function () {
                      var rect = target.getBoundingClientRect(),
                          x = rect.left + (offsetX || (rect.width >> 1)),
                          y = rect.top + (offsetY || (rect.height >> 1)),
                          dataTransfer = { files: this.files };

                      ['dragenter', 'dragover', 'drop'].forEach(function (name) {
                        var evt = document.createEvent('MouseEvent');
                        evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
                        evt.dataTransfer = dataTransfer;
                        target.dispatchEvent(evt);
                      });

                      setTimeout(function () { document.body.removeChild(input); }, 25);
                    };
                    document.body.appendChild(input);
                    return input;
                """
            driver = drop_target.parent
            file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
            file_input.send_keys(path)




        ###############################################################################################
        # sele='#mount_0_0_Ex > div > div > div > div:nth-child(4) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div > div.x15wfb8v.x3aagtl.x6ql1ns.x1iyjqo2.xs83m0k.xdl72j9.xqbdwvv.x1cwzgcd > div.x78zum5.x5yr21d.xl56j7k.x6s0dn4.xh8yej3 > div'
#//*[@id="mount_0_0_Oc"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button
    
        upload_file = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')))
        # self.safe_click(upload_file)                
        # upload_file.drop_files(self.Upload)
        # upload_file.send_keys(self.Upload)
        # path= self.Upload
        drag_and_drop_file(upload_file, path)

        
        # drag_and_drop_file(upload_file)
#         '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button'
# '//*[@id="mount_0_0_jT"]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button'
        try:
            click_to_OK = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'OK')]")))
            self.safe_click(click_to_OK)
        except:
            pass


# # //div[@aria-label='Any time']
        time.sleep(self.SLEEP_SECS)
        Select_crop= WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div')))
        self.safe_click(Select_crop)                    #/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button

        # Select_crop= WebDriverWait(self.driver, 500).until(
        #     EC.visibility_of_element_located((By.XPATH, "//button[@type='button'])")))
        # self.safe_click(Select_crop) 
        time.sleep(self.SLEEP_SECS)
        click_to_Original = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Original')]")))
        self.safe_click(click_to_Original)

        click_to_Next = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Next')]")))
        self.safe_click(click_to_Next)

        click_to_Next = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Next')]")))
        self.safe_click(click_to_Next)

        tag = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea')))
        # '//*[@id="__next"]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/textarea[1]'
        tag.send_keys(Massage)
        time.sleep(self.SLEEP_SECS)


       

        click_to_Share = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Share')]")))
        self.safe_click(click_to_Share)

        

        # try:
        #     for TRY in range(2):
        #         time.sleep(self.SLEEP_SECS)
        #         Try_Again = WebDriverWait(self.driver, 15).until(
        #         EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Try Again')]")))
        #         self.safe_click(Try_Again)
        #         time.sleep(self.SLEEP_SECS)
        # except:
        #     pass
        
        click_to_Share___= WebDriverWait(self.driver, 4000).until(EC.any_of(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Reel shared')]")),
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Post couldn't be shared')]"))))

        # click_to_Share___ = WebDriverWait(self.driver, 500).until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Reel shared')]", "//div[contains(text(),'Post couldn't be shared')]")))
        time.sleep(self.SLEEP_SECS)

        strin_=self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/h1/div').text
                                                   # /html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/h1/div
        print(strin_)

        if strin_=="Post couldn't be shared":
            # instagram.upload(self,Massage,path)
            Try_Again = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Try again')]")))
            self.safe_click(Try_Again)
        else:
            self.safe_click(click_to_Share___)
            time.sleep(self.SLEEP_SECS)
            print('Reel shared')
            time.sleep(5)
            print("DONE>>>")

            self.driver.refresh()

        # click_to_Share___ = WebDriverWait(self.driver, 500).until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Reel shared')]")))
        # time.sleep(self.SLEEP_SECS)

        # try:
        #     post=click_to_Share___.txt
        #     if (post=="Post couldn't be shared"):
        #         time.sleep(self.SLEEP_SECS)
        #         Try_Again = WebDriverWait(self.driver, 15).until(
        #         EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Try Again')]")))
        #         self.safe_click(Try_Again)
        #     self.safe_click(click_to_Share___)
        # except:
        #     pass

        

# Switch back to newly opened tab, which is now in position 0
            # self.driver.switch_to.window(self.driver.window_handles[0])
        

        # WebDriverWait(self.driver, 30).until(EC.url_to_be(self.main_url))

    def safe_click(self, element) -> None:
            retry = 0
            while True:
                with contextlib.suppress(selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.StaleElementReferenceException, selenium.common.exceptions.ElementNotInteractableException, selenium.common.exceptions.ElementClickInterceptedException):
                    element.click()
                    return
                time.sleep(1)
                retry += 1
                if retry > 10:
                    break

def load_Tag() -> List[str]:
    print("Parsing Text.....")
    with open("tag.txt", "r") as fp:
        # print(fp.readlines())
        # return fp.readlines()
        # print(fp.read())
        return fp.read()
        

def get_user_agent() -> str:
    with open("useragents.txt", "r") as fp:
        data = json.loads(fp.read())
    return random.choice(data)["useragent"]

def insta() -> List[str]:
    with open("insta_acount.txt", "r") as fp:
        # print(fp)
        # lines = [line.rstrip('\n') for line in fp]    
           # print(fp.readlines())
        return fp.readlines()
def location() ->  List[str]:
    with open("download_location.txt", "r") as fp:
        # print(fp)
        # lines = [line.rstrip('\n') for line in fp]    
           # print(fp.readlines())
        return fp.readlines()

def main() -> None:
    insta_info= insta()
    print(insta_info)
    user_location=location()
    bot_insta = instagram(username=insta_info[0],password=insta_info[1], SLEEP_SECS=2)
    Tag = load_Tag()
    print(Tag)
    bot_insta.login()
    for i in range(20):
        path=user_location[0]+'colossyan_'+str(i)+'.mp4'
        bot_insta.upload(Tag, path)

if __name__ == "__main__":
    main()

# //*[@id="mount_0_0_ga"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button
# /html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button
# Try Again
# Your post could not be shared. Please try again.
# Post couldn't be shared
# Try again