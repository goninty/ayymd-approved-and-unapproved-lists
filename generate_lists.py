import praw
import re
from settings import *

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT) #praw setup

ayymd = reddit.subreddit('AyyMD')
titles = []
rgx = '(?<=add ).*(?= to)' #regex to find the thing to add to the list


def get_titles(term): #scrape post titles
    for submission in ayymd.search('title:' + term, sort='top'):
        #print(submission.title)
        print(re.search(rgx, (submission.title).lower()).group())
        titles.append(re.search(rgx, (submission.title).lower()).group())

entry = input() #approved or disapproved?
get_titles(entry)
print(titles)