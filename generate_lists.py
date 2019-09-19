import praw
import re
from settings import *

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT) #praw setup

ayymd = reddit.subreddit('AyyMD')
titles = []
links = []
rgxThingName = '(?i)(?<=add ).*(?= to)' #regex to find the thing to add to the list
# TODO
# sort out the god damn instance where the list name is potentially followed by brackets, quotes, etc that then have extra stuff after them
rgxListName = '(?i)(?<=list of )(.*)(?<![.?!])' #regex to find the titles of any lists


def get_title(post, term, rgx): #scrape post titles
    print(re.sub(term+' ', '', re.search(rgx, (post.title)).group()))
    titles.append(re.sub(term+' ', '', re.search(rgx, (post.title)).group()))

def get_link(post): #get the url of the post
    print(post.url)
    links.append(post.url)

entry = input() #approved or disapproved?

for submission in ayymd.search('title:' + entry, sort='top'):
    try:
        get_title(submission, entry, rgxListName)
        if not submission.is_self: #if it's not a text post, grab the link
            get_link(submission)
    except AttributeError:
        pass

#get_titles(entry, rgxListName)
#print(links)