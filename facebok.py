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
import undetected_chromedriver.v2 as uc


class facebook:
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
        self.main_url= 'https://www.facebook.com/login'
        Download= "/home/rinku/Downloads/Wecanwriteatext.mp4"
        self.Upload = '/home/rinku/Downloads/Generated video.mp4'
        self.SLEEP_SECS = 0.5
        
    

    def login(self) -> None:
        print("Log IN......")
        self.driver.get(self.main_url)


        email = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
        email.send_keys(self.username)
        time.sleep(self.SLEEP_SECS)

        password = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]')))
        password.send_keys(self.password)
        time.sleep(self.SLEEP_SECS)

        btn = WebDriverWait(self.driver, 25).until(       
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Log in')]")))
        self.safe_click(btn)                             
        time.sleep(self.SLEEP_SECS)
        # time.sleep(600)
       

        upload_btn = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Photo/video')]")))
        self.safe_click(upload_btn)

        # click_to_Create = WebDriverWait(self.driver, 500).until(
        #     EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Create')]")))
        # self.safe_click(click_to_Create)

        time.sleep(self.SLEEP_SECS)

        Upload = "/home/rinku/Downloads/0_.mp4"
        upload_file = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')))
        # self.safe_click(click_to_Create)
        # Upload = '/home/rinku/Downloads/'+str(k)+'.mp4'
        upload_file.send_keys(Upload)

        click_to_Create = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Post')]")))
        self.safe_click(click_to_Create)
        # upload_file = WebDriverWait(self.driver, 25).until(
        #     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div')))
        # self.safe_click(upload_file)  

        ###############################################################################################
        # def drag_and_drop_file(drop_target, path)-> None:
        #     JS_DROP_FILE = """
        #             var target = arguments[0],
        #                 offsetX = arguments[1],
        #                 offsetY = arguments[2],
        #                 document = target.ownerDocument || document,
        #                 window = document.defaultView || window;

        #             var input = document.createElement('INPUT');
        #             input.type = 'file';
        #             input.onchange = function () {
        #               var rect = target.getBoundingClientRect(),
        #                   x = rect.left + (offsetX || (rect.width >> 1)),
        #                   y = rect.top + (offsetY || (rect.height >> 1)),
        #                   dataTransfer = { files: this.files };

        #               ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        #                 var evt = document.createEvent('MouseEvent');
        #                 evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        #                 evt.dataTransfer = dataTransfer;
        #                 target.dispatchEvent(evt);
        #               });

        #               setTimeout(function () { document.body.removeChild(input); }, 25);
        #             };
        #             document.body.appendChild(input);
        #             return input;
        #         """
        #     driver = drop_target.parent
        #     file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
        #     file_input.send_keys(path)




        ###############################################################################################
        # sele='#mount_0_0_Ex > div > div > div > div:nth-child(4) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div > div.x15wfb8v.x3aagtl.x6ql1ns.x1iyjqo2.xs83m0k.xdl72j9.xqbdwvv.x1cwzgcd > div.x78zum5.x5yr21d.xl56j7k.x6s0dn4.xh8yej3 > div'
#//*[@id="mount_0_0_Oc"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button
            
        #mount_0_0_22 > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j > div > div > div > div.xb57i2i.x1q594ok.x5lxg6s.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.xx8ngbg.xwo3gff.x1n2onr6.x1oyok0e.x1odjw0f.x1e4zzel.x78zum5.xdt5ytf.x1iyjqo2 > div.x78zum5.x1iyjqo2.x1n2onr6.xdt5ytf > div.xexx8yu.x1sxyh0.x18d9i69.xurb0ha > div > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x193iq5w.x1l7klhg.x1iyjqo2.xs83m0k.x2lwn1j.x1y1aw1k.xwib8y2 > div > div > div > div.x78zum5.x1n2onr6.xh8yej3 > div > div > div          
        # upload_file.drop_files(self.Upload)
        # upload_file.send_keys(self.Upload)
        # path= self.Upload
        # drag_and_drop_file(upload_file, path)
        # self.safe_click(click_to_Create)

        post = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//span[contains(text(),'Post')]")))
#         '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button'
# '//*[@id="mount_0_0_jT"]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button'
        try:
            click_to_OK = WebDriverWait(self.driver, 500).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'OK')]")))
            self.safe_click(click_to_OK)
        except:
            pass
# //div[@aria-label='Any time']
        Select_crop= WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button')))
        self.safe_click(Select_crop)                    #/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button

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

        click_to_Share___ = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Reel shared')]")))
        self.safe_click(click_to_Share___)

        time.sleep(self.SLEEP_SECS)
        print('Reel shared')
        time.sleep(5)
        print("DONE>>>")


        

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


def main() -> None:
    bot_insta = facebook(username="918076097914",password="rajkumar@123A", SLEEP_SECS=2)
    # Massage = load_Tag()
    # print(Massage)
    bot_insta.login()
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
