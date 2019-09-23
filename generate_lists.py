# TODO
# remove the lower case-ness (ie keep the original case)
# clean up code
# format into html for webpage

import praw
import re
from settings import *

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT) #praw setup

ayymd = reddit.subreddit('AyyMD')
allLists = {}
titles = []
links = []
rgxListName = re.compile(r'list of ([a-zA-Z\s-]+)', re.I) #regex to find the list name to add thing(s) to
rgxListItem = re.compile(r'(?<= add ).*(?= to )', re.I) #regex to find the thing to add to the list

def get_term(post, term, rgx, grp): #scrape post titles
    #print(re.sub(term, '', re.search(rgx, (post.title)).group(grp), flags=re.IGNORECASE).lower()) #this works, but please god clean it up
    
    return re.sub(term, '', re.search(rgx, (post.title)).group(grp), flags=re.IGNORECASE).lower().strip()

entry = input() #approved or disapproved?

for submission in ayymd.search('title:' + entry, sort='top'):
    try:
        listName = get_term(submission, entry+' ', rgxListName, 1)
        listItem = get_term(submission, entry+' ', rgxListItem, 0)
        
        if listName not in allLists:
            allLists[listName] = []
        allLists[listName].append(listItem)
        
        if not submission.is_self: #if it's not a text post, grab the link
            allLists[listName].append(submission.url)
    except AttributeError:
        pass

for list in allLists:
    print(list + ':' + str(allLists[list]))