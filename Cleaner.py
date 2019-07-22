import praw
import requests

#export
#automate
#whitelist by gilded,subreddit,content,score,awards
#cmd or gui
#delete
#submissions

clientId = ""
clientSecret = ""
userAgent = ""
userName = ""
pw = ""

#connecting to reddit via praw
reddit = praw.Reddit(client_id=clientId,
                     client_secret=clientSecret,
                     password=pw,
                     user_agent=userAgent,
                     username=userName)

def editComments(link):
    comment = reddit.comment(id=link)
    newMessage = "test"     #message that will replace your history
    comment.edit(newMessage)

def getPosts(username):
    link = ("https://api.pushshift.io/reddit/search/comment/?author=" + username)
    r = requests.get(link).json()
    comments = r['data']
    return comments

def editBulkComments(username):
    comments = getPosts(username)
    length = len(comments)
    for data in comments:
        print(data['id'])
