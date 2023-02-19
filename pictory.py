from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from tempfile import mkdtemp
from typing import List
import time
import selenium
import contextlib
import json
import random
import undetected_chromedriver as uc

class pictory:
    def __init__(self, username: str, password: str, SLEEP_SECS: int) -> None:
        self.username = username
        self.password = password
        chrome_options = uc.ChromeOptions()
        # self.main_url = "https://app.pictory.ai/login"
        self.main_url_ = "https://app.pictory.ai/textinput"
        self.main_url= "https://app.pictory.ai/storyboard/scripttovideo"
        self.SLEEP_SECS = 0.10
        chrome_options = Options()
        height = random.randint(600, 980)
        width = random.randint(1000, 1220)
        user_agent = get_user_agent()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument(f'--user-agent={user_agent}')
        chrome_options.add_argument(f'window-size={width}x{height}')
        chrome_options.add_argument("--disable-popup-blocking")
        
        self.driver = uc.Chrome(options=chrome_options, user_data_dir=mkdtemp())

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
        self.driver.get(self.main_url_)


        # try:
        #     cookie_btn = WebDriverWait(self.driver, 25).until(
        #         EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonAccept")))
        #     time.sleep(self.SLEEP_SECS)
        #     self.safe_click(cookie_btn)
        # except:
        #     pass
        try:
            email = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="mui-2"]')))
            email.send_keys(self.username)
            time.sleep(self.SLEEP_SECS)

            password = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="outlined-adornment-password"]')))
            password.send_keys(self.password)
            time.sleep(self.SLEEP_SECS)

            btn = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Login')]")))
            self.safe_click(btn)
            time.sleep(self.SLEEP_SECS)
        except:
            pass
        
        # time.sleep(600)
       
    def create(self, Massage: str, name_of_vi: str) -> None:
        # self.driver.get(self.main_url_)

        Procede = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div[3]/div[1]/div[1]/div[3]/button')))
        self.safe_click(Procede)
        time.sleep(self.SLEEP_SECS)

        video_name = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/main/div/div/div[4]/input')))
        video_name.send_keys(name_of_vi)
        time.sleep(self.SLEEP_SECS)

        Past_your_script = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/main/div/div/div[5]/p')))
        Past_your_script.send_keys(Massage)
        time.sleep(self.SLEEP_SECS)

        Procede = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/main/div/div/div[2]/span[2]/div/div/button[2]')))
        self.safe_click(Procede)
        time.sleep(self.SLEEP_SECS)
  
        #*************** working on hover effect
        hover_select = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Lemon')]")))
        hover = ActionChains(self.driver).move_to_element(hover_select)
        hover.perform()
        time.sleep(self.SLEEP_SECS)

        click_to_Select = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Select')]")))
        self.safe_click(click_to_Select)
        time.sleep(self.SLEEP_SECS)


        # spect_ratio_9_16 = WebDriverWait(self.driver, 500).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "aspect-ratio-card.MuiBox-root.css-79elbk")))
        # self.safe_click(spect_ratio_9_16)
        # time.sleep(self.SLEEP_SECS)
    
    
        # print("Log IN Succesfully......")
        Continue = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Continue')]")))
        self.safe_click(Continue)
        
        time.sleep(self.SLEEP_SECS)
        # time.sleep(30)
        

        # hover_icon = WebDriverWait(self.driver, 500).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "navbar-header")))
        # hover = ActionChains(self.driver).move_to_element(hover_icon)
        # hover.perform()
        # time.sleep(self.SLEEP_SECS)

        

        # WebDriverWait(self.driver, 30).until(EC.url_to_be(self.main_url))
    def next(self) -> None:
        #***************Final Stage
        # self.driver.get(self.main_url)
        # self.driver.get(self.main_url)
        # self.driver.get(self.main_url)
        element = WebDriverWait(self.driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#dropdownMenu2"))) #untill the side-navbar not show
# ?**********************************************

        hover_Setting = WebDriverWait(self.driver, 500).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#dropdownMenu2")))
        hover_S = ActionChains(self.driver).move_to_element(hover_Setting)
        hover_S.perform()
        time.sleep(self.SLEEP_SECS)
        print("Log IN Succesfully......")
        # time.sleep(600)

        # click_to_Hide_Text = WebDriverWait(self.driver, 500).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#scene-setting-dropdown > ul > li:nth-child(4) > label > span")))
        # self.safe_click(click_to_Hide_Text)
        # time.sleep(600)
        # time.sleep(self.SLEEP_SECS)

        print("At span")
        #slider round  #scene-setting-dropdown > ul > li:nth-child(4) > label
        #check box #scene-setting-dropdown > ul > li:nth-child(4) > input

        
        click_to_Hide_Text_all = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#scene-setting-dropdown > ul > li:nth-child(4) > label")))
        self.safe_click(click_to_Hide_Text_all)
        # time.sleep(600)
        # time.sleep(self.SLEEP_SECS) 
        # Generate

        click_to_Hide_Text_all = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#scene-setting-dropdown > ul > li:nth-child(4) > input")))
        self.safe_click(click_to_Hide_Text_all)
        # time.sleep(600)
        time.sleep(self.SLEEP_SECS) 


        Generate = WebDriverWait(self.driver, 500).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#generate-button-dropdown")))
        hover_gen = ActionChains(self.driver).move_to_element(Generate)
        hover_gen.perform()
        time.sleep(self.SLEEP_SECS)
       

        Video = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="btnGenerate"]')))
        self.safe_click(Video)
        time.sleep(self.SLEEP_SECS)
        #btnGenerate


        # wait_for_Download= WebDriverWait(self.driver, 2000000).until(
        #     EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Download')]")))
        # time.sleep(self.SLEEP_SECS)  
        # self.safe_click(wait_for_Download)

        wait = WebDriverWait(self.driver, 50000000000000).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="GenerateVideoPopuptext2"]/span/span')))
        self.safe_click(wait)
        time.sleep(self.SLEEP_SECS)
    # def video(self) -> None:
        # Pictory.login(self)
        # self.driver.get('https://app.pictory.ai/myvideos')
        menu = WebDriverWait(self.driver, 50000000000000).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="long-button"]')))
        self.safe_click(menu)
        time.sleep(self.SLEEP_SECS)

        wait = WebDriverWait(self.driver, 50000000000000).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Download')]")))
        self.safe_click(wait)
        time.sleep(self.SLEEP_SECS)

        mp4 = WebDriverWait(self.driver, 50000000000000).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="long-menu"]/div[3]/ul/li[1]')))
        self.safe_click(mp4)
        time.sleep(self.SLEEP_SECS)


        print("please wait for one minut")
       
        time.sleep(60)
# //*[@id="long-button"]
# //*[@id="long-menu"]/div[3]/ul/li[1] mp4
# //*[@id="long-button"] menu 
# My projects
# https://app.pictory.ai/myvideos
# //*[@id="long-button"] #long-button

    def emotion(self, Massage: list):
        content=[]
        for msg in Massage:
            self.driver.get('https://www.travpart.com/English/emotion-ai/')
            Past_your_script = WebDriverWait(self.driver, 500).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="w3review"]')))
            Past_your_script.send_keys(msg)

            Check = WebDriverWait(self.driver, 500).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="content "]/div/div/div/form/input')))
            self.safe_click(Check)
            time.sleep(self.SLEEP_SECS)  

            # String_text = self.driver.findElement(By.xpath('//*[@id="content "]/div/div/div/h3[1]')).getText();

            # strin=self.driver.find_element(By.XPATH, '//*[@id="content "]/div/div/div/h3[1]').text
            strin_=self.driver.find_element(By.XPATH, '//*[@id="content "]/div/div/div/h3[3]').text
            # print(strin.split(" ")[-1])
            # S=strin.split(" ")[-1]
            S_= strin_.split(" ")[-1]
            print(S_)
            
            if (str(S_)=='Emotional' or str(S_)=='EmotionalContext'):
                content.append(str(msg))
                print("Content is Emotional...\n")
            else:
                print("Content is Not Emotional...\n")
                # print("Exit.........")
                # exit()
        # with open("colosian.txt", "w") as file:
        #     file.write(content)
        print('content.........',   content)
        text_file = open("col.txt", 'w')
        for i in content:
            # text_file.write(i + '\n')
            text_file.write(i)
        return(content)
            # print(String_text)
def load_massage() -> List[str]:
    print("Parsing Text.....")
    with open("massage.txt", "r") as fp:
        # print(fp)
        # lines = [line.rstrip('\n') for line in fp]    
           # print(fp.readlines())
        return fp.readlines()
        # print(fp.read())
        # return lines

def get_user_agent() -> str:
    with open("useragents.txt", "r") as fp:
        data = json.loads(fp.read())
    return random.choice(data)["useragent"]


def pictory_info() ->  List[str]:
    with open("pictory_acount.txt", "r") as fp:
        # print(fp)
        # lines = [line.rstrip('\n') for line in fp]    
           # print(fp.readlines())
        return fp.readlines()



def main() -> None:
#************************************************
    pictory_account_info= pictory_info()  
    print(pictory_account_info)
    
#************************************************

    bot = pictory(username=pictory_account_info[0],password=pictory_account_info[1], SLEEP_SECS=2)
    Massage = load_massage()

    Emo=bot.emotion(Massage)

    print("Content is....",Emo)
    l=0
   
    for Msg in (Emo):
        print('mass is', Msg)
        print(l)
        name_of_vi= 'pictory_'+str(l)
        # pictory_0.mp4
        print(name_of_vi)

        bot.login()
        bot.create(Msg,name_of_vi)
        bot.next()
        # bot.video()
        l=1+l
    time.sleep(90)
    print('All video scccesfully generated run colossyan file...')
if __name__ == "__main__":
    main()


# <label for="responses_2865807_4737821">
#       <input id="responses_2865807_4737821" name="responses[2865807][]" type="checkbox" value="4737821">
# "
#       Yes
# "
# </label>

# driver.find_element_by_xpath("//label/input[contains(..,'Yes')]").click()
