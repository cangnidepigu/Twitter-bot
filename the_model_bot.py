# themodelbot

import tweepy as tp
import time
import os
import random

# credentials to login to twitter api
consumer_key = '#'
consumer_secret = '#'
access_token = '#-#'
access_secret = '#'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)


os.chdir('models')



# tries to randomly choose from given dir
for media_image in os.listdir('.'):
    api.update_with_media(random.choice(os.listdir()))
    print('UPLOADED')
    
    time.sleep(10)
    
'''
das an original one

for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(5)
'''

