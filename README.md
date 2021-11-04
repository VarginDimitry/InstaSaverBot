# InstaSaverBot
This telegram bot helps to download any photo from Instagram

If you have some ideas to upgrade this bot, then write me
in telegram @dmitryvargin

## Exceptions

The bot downloads single photo easily, but it can download only
a part of photo series and the bot can not download a video at all.

## Installation

1) Clone this rep to your computer
2) Create a config file in the root of project. Name it "config.json".
3) Then you shall write:


    {
        "API_TOKEN": "*your token from BotFather*",
        "admins": ["IDs of users which will be admins"]
    }

4) Download "chromedriver" (Selenium webdriver) 
and put it in our dictionary
(link: https://sites.google.com/chromium.org/driver/)
5) Install requirements:


    pip install -r requirements.txt

6) Run it in ***main.py***
