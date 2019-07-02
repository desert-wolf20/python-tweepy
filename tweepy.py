import tweepy
import time
from pprint import pprint
class Add_accounts():

  
    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        
        
        self.consumer_key = consumer_key

        self.consumer_secret = consumer_secret
       
        self.access_token = access_token
      
        self.access_token_secret = access_token_secret
       
        ## authintication
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        me = api.me()
        rate_l = api.rate_limit_status()
        print (me.name)
        pprint (rate_l)
        print(me.location)
        
        options_n = input('What do you want to do? (Enter an number) \n(1) DELET TWEETS\n(2) RETWEET \n(3) FAVORITES \n(4) Follow who tweets in specifec hashtag\n(5) Follow someones followers  ')
        if options_n == '1':
            #delet Tweet
            items_n = input('How many tweets do you want to DELETE?')
            for status in tweepy.Cursor(api.user_timeline).items(int(items_n)):
                try:
                    api.destroy_status(status.id)
                    print ("Deleted:", status.id)
                except:
                    print ("Failed to delete:", status.id)
        elif options_n == '2':
            #reteet
            tweet_id = input('What is the tweet ID?')
            api.retweet(int(tweet_id))
            print('DONE')
        elif options_n == '3':
            #favorite
            tweet_id = input('What is the tweet ID?')
            api.create_favorite(int(tweet_id))
            print('DONE')
        elif options_n == '4':   
            q = input('What is Hashtage to follow?')
            num = input('How many to follow ?')
            for follower in tweepy.Cursor(api.search, q, result_type='recent').items(num):
                api.create_friendship(screen_name = follower.author.screen_name)
                print(follower.author.screen_name)
                time.sleep(5) #SECONDS
        elif options_n == '5':
            acount_F = input('what is the account ')
            user = api.get_user(acount_F)
            print("ACCOUNT NAME", user.screen_name)
            print("ACCOUNT FOLLOWERS", user.followers_count)
            for friend in user.followers():
                api.create_friendship(friend.screen_name)
                print("following ",user.screen_name,": ", friend.screen_name)
                time.sleep(5)

#replace your creditinal info
myAccount = Add_accounts('consumer_key','consumer_secret','access_token','access_token_secret')
