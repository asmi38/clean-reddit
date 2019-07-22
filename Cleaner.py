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
