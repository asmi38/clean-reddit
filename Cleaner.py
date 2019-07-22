import praw
import requests
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

#export
#automate
#whitelist by gilded,subreddit,content,score,awards
#cmd or gui
#delete
#submissions


#connecting to reddit via praw
reddit = praw.Reddit(client_id=config.get("connection", "client_id"),
                     client_secret=config.get("connection", "client_secret"),
                     password=config.get("connection", "password"),
                     user_agent=config.get("connection", "user_agent"),
                     username=config.get("connection", "username"))


def getComments(username):
    link = ("https://api.pushshift.io/reddit/search/comment/?author=" + username)
    r = requests.get(link).json()
    comments = r['data']
    return comments

def editComments(link):
    comment = reddit.comment(id=link)
    newMessage = "new comment here"
    comment.edit(newMessage)

def deleteComents(link):
    comment = reddit.comment(id=link)
    comment.delete()

def exportComment(link):

def editBulkComments(username):
    comments = getComments(username)
    length = len(comments)
    for data in comments:
        print(data['id'])
