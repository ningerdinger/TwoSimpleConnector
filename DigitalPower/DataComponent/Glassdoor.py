from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import WritingToDB as wDB


class Glassdoor:
    ''' This application will gather data from glassdoor. You just need to specify the job function

        Args:
            path: the location of your chromedriver.exe
            pages: specifies how many pages worth of data needs to be retrieved
            key_token: the dropbox token
            key_word: the job function you want to search.
                Make sure the variable is given in the form of "data-science" i.e.
                no capitals and use '-' hyphens for spaces
    '''
    def __init__(self, path: str, pages: int, key_token: str, key_word: str):
        self.key = key_token
        self.url = f'https://www.glassdoor.co.in/Job/netherlands-{key_word}-jobs-SRCH_IL.0,11_IN178_KO12,24.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data%2520science&typedLocation=Netherlands&context=Jobs&dropdown=0'
        self.path = path
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=path, options=self.options)
        self.driver.get(self.url)
        self.pages_count=1

        #We keep looping for pages until the amount of pages has reached the amount specified in the input parameter
        try:
            while self.pages_count<=pages:
                time.sleep(2)
                print(f"Scraping page{self.pages_count}")
                self.Logic(self.pages_count)
                self.pages_count = self.pages_count + 1
        except NoSuchElementException:
            print('Check whether the page has any more pages left')
        self.driver.quit()

    def Logic(self, page: int):
        ''' This method is the logic that goes over the jobs available on Glassdoor

            Args:
                page: specify how many pages you want to retrieve
        '''
        data_set = self.driver.find_element(By.XPATH, '//*[@id="MainCol"]/div[1]/ul')
        data_in_text = str(data_set.text)
        #I added time.sleep(2) since depending on your internet speed, it may not have fully loaded yet which would can lead to an error
        time.sleep(2)
        text_file = open(f"page{page}.txt", "w", encoding="utf-8")
        time.sleep(2)
        text_file.write(data_in_text)
        text_file.close()
        #Path within my storage
        target_path = '/DigitalPowerCBSData/Bronze/glassdoor'
        wDB.WritingToDB(
            name=f"page{page}",
            target_path=target_path,
            key=self.key,
            file_format='txt'
            )
        time.sleep(2)
        button = self.driver.find_element(
            By.XPATH, 
            '//*[@id="MainCol"]/div[2]/div/div[1]/button[7]'
            )
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)


path = '<path to chromedriver.exe>'
token = "<Your dropbox token>"
Glassdoor(path, 5, token, 'data-science')
