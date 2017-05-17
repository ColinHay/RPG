#RPG - Reddit Post Getter#
#           2.0          #          
##########################

#import modules
import praw
import time
from slacker import Slacker

#create reddit instance
reddit = praw.Reddit(client_id='vaBsxDjQvk5jWA',
                     client_secret='81M6u2rXtrP-kGF1KKg99LSwRuY',
                     user_agent='Windows:RPG:2.0 (by /u/coli_ha)')

#connect to slack
slack = Slacker('xoxb-183678733280-v4ZLYDSWPOGVDzwbvfLLfZB2')

#Lists of subreddits, keywords, and posted items as well as a dictionary for newPosts
subreddits = ['space', 'astronomy', 'astrophotography',
              'cosmos', 'cosmology', 'telescopes',
              'moon', 'comets']

keywords = ['space', 'telescope', 'slooh',
            'moon', 'eclipse', 'astronomy',
            'planet']

newPosts = {}
posted = []

while True:
    #For loops populate newPosts dictionary with relevant data
    for subredditName in subreddits:
        for post in reddit.subreddit(subredditName).new(limit=10):
            for keyword in keywords:
                if keyword in post.title:
                    if post.id not in newPosts :
                        newPosts.update({post.id:'\n\n\n----------\n/r/'+subredditName+'\n'+post.title+'\nhttps://www.reddit.com/r/'+subredditName+'/comments/'+post.id+'\n----------'})

    #For loop prints gathered data to console and adds it to posted list
    for id in newPosts:
        if id not in posted:
            posted.append(id)
            print(newPosts[id])
            slack.chat.post_message('#test', newPosts[id])

    #Refresh timer
    time.sleep(600)
