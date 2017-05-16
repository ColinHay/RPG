#RPG - Reddit Post Getter#
#           1.0          #          
##########################

#import praw
import praw

#create reddit instance
reddit = praw.Reddit(client_id='vaBsxDjQvk5jWA',
                     client_secret='81M6u2rXtrP-kGF1KKg99LSwRuY',
                     user_agent='Windows:RPG:1.0 (by /u/coli_ha)')

#Lists of subreddits and keywords to use
subreddits = ['space', 'astronomy', 'astrophotography',
              'cosmos', 'cosmology', 'telescopes',
              'moon', 'comets']

keywords = ['space', 'telescope', 'slooh',
            'moon', 'eclipse', 'astronomy']

#For loops for printing relevant data
for subredditName in subreddits:
    print('')
    print('==========')
    print('/r/'+subredditName)
    print('==========')
    for post in reddit.subreddit(subredditName).new(limit=10):
        for keyword in keywords:
            if keyword in post.title:
                print(post.title)
                print('https://www.reddit.com/r/'+subredditName+'/comments/'+post.id)
                print('')
