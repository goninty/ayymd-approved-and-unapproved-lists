# TODO
# remove the lower case-ness (ie keep the original case)
# clean up code
# some shit get truncated i think (some links)

import praw
import re
from settings import *

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT) #praw setup

ayymd = reddit.subreddit('AyyMD')
allLists = {}
rgxListName = re.compile(r'list of ([a-zA-Z0-9\s-]+)', re.I) #regex to find the list name to add thing(s) to
rgxListItem = re.compile(r'(?<= add ).*(?= to )', re.I) #regex to find the thing to add to the list

def get_term(post, term, rgx, grp): #scrape post titles
    return re.sub(term, '', re.search(rgx, (post.title)).group(grp), flags=re.IGNORECASE).strip()

def get_all_lists():
    return allLists

entry = input() #approved or disapproved?

for submission in ayymd.search('title:' + entry, sort='top', limit=1000):
    try:
        listName = get_term(submission, entry+' ', rgxListName, 1)
        listItem = get_term(submission, entry+' ', rgxListItem, 0)
        
        if listName not in allLists:
            allLists[listName] = {}
        
        if not submission.is_self: #if it's not a text post, grab the link
            allLists[listName][listItem] = submission.url
        else:
            allLists[listName][listItem] = '#'
    except AttributeError:
        pass