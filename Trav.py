from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#from con import write_data
from connection import write_data
from tempfile import mkdtemp
from bs4 import BeautifulSoup
from typing import List
import time
import selenium
import contextlib
import json
import random
import undetected_chromedriver.v2 as uc

# chrome_options = Options()
# chrome_options.add_argument("user-data-dir=selenium") 
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("www.google.com")



def load_massage() -> List[str]:
    print("Parsing Text.....")
    with open("massage.txt", "r") as fp:
        # print(fp.readlines())
        # return fp.readlines()
        # print(fp.read())
        return fp.read()
        

def get_user_agent() -> str:
    with open("useragents.txt", "r") as fp:
        data = json.loads(fp.read())
    return random.choice(data)["useragent"]


class Pictory:
    def __init__(self, username: str, password: str, SLEEP_SECS: int) -> None:
        self.username = username
        self.password = password
        chrome_options = uc.ChromeOptions()
        # self.main_url = "https://app.pictory.ai/login"
        # self.main_url = "https://app.pictory.ai/textinput"
        self.main_url= "https://www.travpart.com/English/timeline/"
        Download= "/home/rinku/Downloads/Wecanwriteatext.mp4"
        self.Upload = '/home/rinku/Downloads/Generated video.mp4'
        self.SLEEP_SECS = 0.45
        chrome_options = Options()
        height = random.randint(600, 980)
        width = random.randint(1000, 1220)
        user_agent = get_user_agent()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument(f'--user-agent={user_agent}')
        chrome_options.add_argument(f'window-size={width}x{height}')
        chrome_options.add_argument("--disable-popup-blocking")
        
        self.driver = uc.Chrome(options=chrome_options,
                                user_data_dir=mkdtemp())

#  with suppress(SpecificError): do_something() says don't propagate the error if it is raised while doing something
#  try: do_something() except SpecificError: pass says do something and don't propagate the error if it is raised

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

    def login(self) -> None:
        print("Log IN......")
        self.driver.get('https://www.travpart.com/English/login/')

        # try:
        #     cookie_btn = WebDriverWait(self.driver, 25).until(
        #         EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonAccept")))
        #     time.sleep(self.SLEEP_SECS)
        #     self.safe_click(cookie_btn)
        # except:
        #     pass

        email = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="username-14250"]')))
        email.send_keys(self.username)
        time.sleep(self.SLEEP_SECS)

        password = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user_password-14250"]')))
        password.send_keys(self.password)
        time.sleep(self.SLEEP_SECS)

        btn = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="um-submit-btn"]')))
        self.safe_click(btn)
        time.sleep(self.SLEEP_SECS)
        # time.sleep(600)
       

        self.driver.get(self.main_url)

        Procede = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content "]/div/div/div[1]/div[2]/button')))
        self.safe_click(Procede)
        time.sleep(self.SLEEP_SECS)

        Past_your_script = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Photo/Video')]")))
        self.safe_click(Past_your_script)
        time.sleep(self.SLEEP_SECS)



        # time.sleep(600)
       

        

        # time.sleep(self.SLEEP_SECS)


        ###############################################################################################
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
        def drag_and_drop_file(drop_target, path)-> None:
            driver = drop_target.parent
            file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
            file_input.send_keys(path)


        upload_file = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__wp-uploader-id-0"]/div[3]/div[2]')))
        path= self.Upload
        drag_and_drop_file(upload_file, path)

        
        # self.safe_click(upload_file)                
        # upload_file.drop_files(self.Upload)
        # upload_file.send_keys(self.Upload)
        

        confirm = WebDriverWait(self.driver, 500).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__wp-uploader-id-3"]/div[4]/div/div[2]/button')))
        self.safe_click(confirm)



        publish = WebDriverWait(self.driver, 500).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="createpostModal"]/div/div/div/div/header/div/div[3]/div[2]/div[2]/button[1]')))
        self.safe_click(confirm)

        ###############################################################################################
        # sele='#mount_0_0_Ex > div > div > div > div:nth-child(4) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div > div.x15wfb8v.x3aagtl.x6ql1ns.x1iyjqo2.xs83m0k.xdl72j9.xqbdwvv.x1cwzgcd > div.x78zum5.x5yr21d.xl56j7k.x6s0dn4.xh8yej3 > div'
#//*[@id="mount_0_0_Oc"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button
        
#         '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button'
# '//*[@id="mount_0_0_jT"]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button'
#         try:
#             click_to_OK = WebDriverWait(self.driver, 500).until(
#                 EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'OK')]")))
#             self.safe_click(click_to_OK)
#         except:
#             pass
# # //div[@aria-label='Any time']
#         Select_crop= WebDriverWait(self.driver, 500).until(
#             EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button')))
#         self.safe_click(Select_crop)                    #/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button

#         click_to_Original = WebDriverWait(self.driver, 500).until(
#             EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Original')]")))
#         self.safe_click(click_to_Original)

#         click_to_Next = WebDriverWait(self.driver, 500).until(
#             EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Next')]")))
#         self.safe_click(click_to_Next)

#         click_to_Next = WebDriverWait(self.driver, 500).until(
#             EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Next')]")))
#         self.safe_click(click_to_Next)

#         tag = WebDriverWait(self.driver, 25).until(
#             EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea')))
#         # '//*[@id="__next"]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/textarea[1]'
#         tag.send_keys(Massage)
#         time.sleep(self.SLEEP_SECS)

#         click_to_Share = WebDriverWait(self.driver, 500).until(
#             EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Share')]")))
#         self.safe_click(click_to_Share)

#         click_to_Share___ = WebDriverWait(self.driver, 500).until(
#             EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Reel shared')]")))
#         self.safe_click(click_to_Share___)

#         time.sleep(self.SLEEP_SECS)
#         print('Reel shared')
#         time.sleep(5)
#         print("DONE>>>")

def main() -> None:
    bot = Pictory(username="RAJ_DAS",password="raj@123A", SLEEP_SECS=2)
    # Massage = load_massage()
    # bot.emotion(Massage)
    # print(Massage)
    bot.login()
    # bot.next()
   


if __name__ == "__main__":
    main()


# <label for="responses_2865807_4737821">
#       <input id="responses_2865807_4737821" name="responses[2865807][]" type="checkbox" value="4737821">
# "
#       Yes
# "
# </label>

# driver.find_element_by_xpath("//label/input[contains(..,'Yes')]").click()
