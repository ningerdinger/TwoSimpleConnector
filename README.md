# TwoSimpleConnector

In this application, I built two simple pipelines. The first pipeline retrieves data from CBS and converts it into a JSON format. It will then upload it to Dropbox. The second data source is from Glassdoor. I made a webscraper that retrieves some of the html code and transforms it into readable text. It is formed into a txt file format. After it has done so, it will store the data on dropbox. 

I opted to go for dropbox since it is free, however it doesn't support many of the functionalities and services like the big Cloud providers does (AWS, Google and Azure). Furthermore, keep in mind that this is an unfinished work. In the Powerpoint I have elaborated on how the more elaborate (simple) design should look like. 

To do:

Setting up Dropbox

1)You will require a dropbox account

2)Go to Dropbox developer's app here https://www.dropbox.com/lp/developers

3)Click on top right "Developer's console"

4)Create your new app by clicking "Create app"

5)Choose "Full Dropbox" access. All other options should not be available with free account

6)You are free to name your app

7)Enter your app. You will see the tabs; settings, permissions, branding and analytics. Please head over to settings

8)Enable the permissions with respect to reading and writing. See image for the ones you have to turn on
![image](https://user-images.githubusercontent.com/52888356/184003935-a8bd4b33-dc8f-4de4-a142-1fe17c94670c.png)

9)Head back to settings and scroll down to "Generated access token". Click generate.

10)Copy this token and put it in the token variable in CBS.py and Glassdoor.py

**Note that dropbox token only lasts for 4 hours. After that you will have to refresh it**


Glassdoor.py will require chromedriver.exe to work. Please download it here; https://chromedriver.chromium.org/downloads. Also make sure that the appropiate version of Google chrome is downloaded. The version needs to be compatible with the chromedriver version you downloaded. Instruction is on the chromedriver page.

After downloading specify the path to your chromedriver.exe in Glassdoor.py

**Keep in mind that line 17 and 18 of CBS.py are commented out because otherwise it would be too much data. In lieu of that I toke only a very small sample size (3 identifiers). The code "cbsodata.get_table_list()" will return metadata of all identifiers.**
















