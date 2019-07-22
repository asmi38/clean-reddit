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
