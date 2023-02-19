from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#from con import write_data

from tempfile import mkdtemp
from typing import List
import time
import selenium
import contextlib
import json
import random
import undetected_chromedriver as uc


class colossyan:
    def __init__(self, username: str, password: str, SLEEP_SECS: int) -> None:
        self.username = username
        self.password = password
        chrome_options = uc.ChromeOptions()
        self.main_url = "https://app.colossyan.com/"
        self.main_url_1='https://app.colossyan.com/my-videos'
        # self.upload = 
        self.SLEEP_SECS = 0.2
        chrome_options = Options()
        height = random.randint(800, 1080)
        width = random.randint(1800, 1920)
        user_agent = get_user_agent()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument(f'--user-agent={user_agent}')
        chrome_options.add_argument(f'window-size={width}x{height}')
        chrome_options.add_argument("--disable-popup-blocking")

        # chrome_options.add_experimental_option("prefs", {"download.default_directory": "/home/rinku/Downloads/Persepolis/Audios"})
        # prefs = {'download.default_directory' : Download}
        # chrome_options.add_experimental_option('prefs', prefs)

        # chrome_options.add_argument('download.default_directory'+Download)
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
        self.driver.get(self.main_url)

      
        email = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
        email.send_keys(self.username)
        time.sleep(self.SLEEP_SECS)

        password = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
        password.send_keys(self.password)
        time.sleep(self.SLEEP_SECS)

        btn = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/section/div/div/div/form/div[2]/button')))
        self.safe_click(btn)
        
       
        print("Log IN Succesfully......")
        time.sleep(self.SLEEP_SECS)


    def Script_actor(self, Massage: str, Acc: str) -> None:
        self.driver.get(self.main_url)
        
        # dropdown.send_keys(Keys.ENTER)
        

        New = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[1]/div[1]/div/button[1]')))
        self.safe_click(New)

        try:
            New = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Start from Scratch')]")))
            self.safe_click(New)
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass

        # actor = WebDriverWait(self.driver, 25).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption css-10oplfw' and contains(., 'Script')]")))
        # self.safe_click(actor)

        time.sleep(self.SLEEP_SECS)
        
        Msg = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div[1]/div')))
        # '//*[@id="__next"]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/textarea[1]'
        Msg.send_keys(Massage)
        time.sleep(self.SLEEP_SECS)


        actor = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Actor')]")))
        self.safe_click(actor)
        time.sleep(self.SLEEP_SECS)
 
        chang = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-1rc505s")))
        self.safe_click(chang)
        time.sleep(self.SLEEP_SECS)

# ***************************************************************************************************


        select_actor = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '"+Acc+"')]")))
        self.safe_click(select_actor)

        Untitled_video = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Untitled video')]")))
        self.safe_click(Untitled_video)
        time.sleep(self.SLEEP_SECS)

        Set_scene_size = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Set scene size')]")))
        self.safe_click(Set_scene_size)
        time.sleep(self.SLEEP_SECS)

        Instagram_story = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Instagram story')]")))
        self.safe_click(Instagram_story)
        time.sleep(self.SLEEP_SECS)


        Actor_position_down = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/button')))
        self.safe_click(Actor_position_down)
        time.sleep(self.SLEEP_SECS)



        
    
                
       

    def background(self, Upload: str) -> None:
        
        # self.driver.get("https://app.colossyan.com/drafts/a3ab1b65-bf2e-44d1-b608-4c5c757af45f")
    
        # dropdown.send_keys(Keys.ENTER)
        # advance_setting = WebDriverWait(self.driver, 25).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "MuiBox-root.css-1epvwmu")))
        # self.safe_click(advance_setting)
        background_menu = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Background')]")))
        self.safe_click(background_menu)
        time.sleep(self.SLEEP_SECS)
        
        upload = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Uploads')]")))
        self.safe_click(upload)
        time.sleep(self.SLEEP_SECS)

        upload_file = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        
        # elem = driver.find_element_by_xpath("//input[@type='file']")
        # elem.send_keys("C:\\full\\path\to\\video.mp4"); # Window$
        upload_file.send_keys(Upload) # Linux


        wait_for_upload = WebDriverWait(self.driver, 2000000).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Uploaded ')]")))
        time.sleep(self.SLEEP_SECS)


        menu_video = WebDriverWait(self.driver, 2000000).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/button')))
        self.safe_click(menu_video)

        
        slider_volume = WebDriverWait(self.driver, 2000000).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/span/span[3]'))) #Selecting all sliders
        move = ActionChains(self.driver)
        move.click_and_hold(slider_volume).move_by_offset(50, 0).release().perform()


        

        # music = WebDriverWait(self.driver, 25).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Music')]")))
        # self.safe_click(music)
        # time.sleep(self.SLEEP_SECS)

        # select_music = WebDriverWait(self.driver, 2000000).until(
        #     EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div/div[2]/ul/li[2]/button')))
        # self.safe_click(select_music)
        
        print("Background")
    # *****************************************************************************************
    def video_Genration(self, name_video: str) -> None:

        Generate = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Generate')]")))
        self.safe_click(Generate)
        time.sleep(self.SLEEP_SECS)

        # click_on = WebDriverWait(self.driver, 25).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Generate')]")))
        # self.safe_click(Generate)
        # time.sleep(self.SLEEP_SECS)

        # level_title = WebDriverWait(self.driver, 25).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-15n88l1 > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div > div.MuiFormControl-root.MuiFormControl-fullWidth.MuiTextField-root.css-1s6dx3o > div")))
        # #"//label[contains(text(),'Title')]"
        # self.safe_click(level_title)
        # time.sleep(self.SLEEP_SECS)

        name_vid = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Title']")))
        name_vid.send_keys(name_video)
        # try:
            
        # except:
        #     pass
        
        subtitle_add = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-15n88l1 > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div > div:nth-child(3) > span"))) #Selecting all sliders
        self.safe_click(subtitle_add)

        # subtitle_add = WebDriverWait(self.driver, 25).until(
        #     EC.visibility_of_element_located((By.XPATH, "/html/body/div[9]/div[3]/div/div/div[2]/span"))) #Selecting all sliders
        # self.safe_click(subtitle_add)
        # move.click_and_hold(subtitle_add).move_by_offset(0, 0).release().perform()


        one_eighty= WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '1080')]")))
        self.safe_click(one_eighty)
        time.sleep(self.SLEEP_SECS)

        seven_twenty = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '720p')]")))
        self.safe_click(seven_twenty)
        time.sleep(self.SLEEP_SECS)

        Start_generation = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Start generation')]")))
        self.safe_click(Start_generation)
        time.sleep(self.SLEEP_SECS)

        # Click_progress = WebDriverWait(self.driver, 2500000000).until(
        #     EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Click here to check the progress.)]")))
        # self.safe_click(Click_progress)
        # time.sleep(self.SLEEP_SECS)

        
        print("done")

        time.sleep(10)

    def My_video(self) -> None:
        print("inside_country")
        self.driver.get(self.main_url_1)

        menu = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div[2]/button')))
        self.safe_click(menu)
        time.sleep(self.SLEEP_SECS)

        Click_progress = WebDriverWait(self.driver, 25000000000000000).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Download')]")))
        self.safe_click(Click_progress)

        

        time.sleep(240)
# ******************************************************
        # actor_setting = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div/div/div[4]/button')))
        # self.safe_click(select_actor)

        # Lyout = WebDriverWait(self.driver, 25).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="mui-191"]')))
        # Lyout.send_keys(1500)
        # time.sleep(self.SLEEP_SECS)
        # driver.find_element_by_xpath("//option[@value='" + state + "']").click()
        # editor = WebDriverWait(self.driver, 30).until(
        # EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div')))
        # print("inside_country_Exit")
        # time.sleep(100)
        
def load_massage() -> List[str]:
    print("Parsing countries.....")
    with open("col.txt", "r") as fp:
        # print(fp.readlines())
        return fp.readlines()

def get_user_agent() -> str:
    with open("useragents.txt", "r") as fp:
        data = json.loads(fp.read())
    return random.choice(data)["useragent"]

def colossyan_info() -> str:
    with open("colossyan_account.txt", "r") as fp:
        # print(fp)
        # lines = [line.rstrip('\n') for line in fp]    
           # print(fp.readlines())
        return fp.readlines()

def location() ->  str:
    with open("download_location.txt", "r") as fp:
        # print(fp)
        # lines = [line.rstrip('\n') for line in fp]    
           # print(fp.readlines())
        return fp.readlines()

def main() -> None:
    col_account_info= colossyan_info()
    Msg = load_massage()
    user_location=location()
    print(col_account_info)
    bot = colossyan(username = col_account_info[0], password = col_account_info[1], SLEEP_SECS=2)
    # actor = input("Please select the actor Like Shruti:  ")
    bot.login()
    c=0
    for Massage in Msg:
        print(Massage)
        Upload = user_location[0]+'pictory_'+str(c)+'.mp4'
        print(Upload)
        name_video = 'colossyan_'+str(c)
        print(Upload)
        print(name_video)

        bot.Script_actor(Massage, 'Harini')
        bot.background(Upload)
        bot.video_Genration(name_video)
        bot.My_video()

        c=c+1
        print(k)
       


if __name__ == "__main__":
    main()