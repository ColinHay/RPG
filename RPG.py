#RPG - Reddit Post Getter#
#           2.2          #          
##########################

#import modules
import praw
import time
from slacker import Slacker

#create reddit instance
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

#connect to slack
slack = Slacker('')

#Lists of subreddits and keywords which should be populated before running
subreddits = []
keywords = []

#NewPosts is a dictionary to hold data about new posts, posted keeps track of
#what posts have been pushed to Slack to avoid duplicate posts
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
