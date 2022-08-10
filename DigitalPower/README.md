# DigitalPower

In this application, I built two simple pipelines. The first pipeline retrieves data from CBS and converts it into a JSON format. It will then upload it to Dropbox. I opted to go for dropbox since it is free, however it doesn't support writing data into its storage directly like various Cloud services does.

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

9)Head back to settings and down below you will see "Generated access token". Click generate.

10)Copy this token and put it in the token variable in CBS.py and Glassdoor.py

Glassdoor.py will require chromedriver.exe to work. Please download it here; https://chromedriver.chromium.org/downloads. Also make sure that the appropiate version of Google chrome is downloaded. The version needs to be compatible with the chromedriver version you downloaded. Instruction is on the chromedriver page.

After downloading specify the path to your chromedriver.exe in Glassdoor.py


















![image](https://user-images.githubusercontent.com/52888356/184003935-a8bd4b33-dc8f-4de4-a142-1fe17c94670c.png)
