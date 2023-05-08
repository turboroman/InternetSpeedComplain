from os import environ

from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 200
PROMISED_UP = 20
TWITTER_EMAIL = environ.get('TWITTER_EMAIL')
TWITTER_PASSWORD = environ.get('TWITTER_PASSWORD')
TWITTER_USERNAME = environ.get('TWITTER_USERNAME')

internet_bot = InternetSpeedTwitterBot()

speeds = internet_bot.get_internet_speed()

if speeds['down'] < 200 or speeds['up'] < 20:
    internet_bot.login_twitter(tw_email=TWITTER_EMAIL,
                               tw_password=TWITTER_PASSWORD,
                               tw_username=TWITTER_USERNAME)
    internet_bot.write_tweet(speeds['down'], speeds['up'])
