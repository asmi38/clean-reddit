import praw
import requests
import csv
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

#automate
#whitelist by gilded,subreddit,content,score,awards
#delete
#submissions

#connecting to reddit via praw
reddit = praw.Reddit(client_id=config.get("connection", "client_id"),
                     client_secret=config.get("connection", "client_secret"),
                     password=config.get("connection", "password"),
                     user_agent=config.get("connection", "user_agent"),
                     username=config.get("connection", "username"))

def get_comments(username):
    link = ("https://api.pushshift.io/reddit/search/comment/?author=" + username)
    r = requests.get(link).json()
    comments = r['data']
    return comments

def edit_comments(link):
    comment = reddit.comment(id=link)
    newMessage = "new comment here"
    comment.edit(newMessage)

def delete_coments(link):
    comment = reddit.comment(id=link)
    comment.delete()

def export_comment(comment):
    values = [comment['author'], comment['subreddit'], comment['body']]
    comment_data = open('CommentData.csv', 'a') #open file for writing
    csvwriter = csv.writer(comment_data)
    csvwriter.writerow(values)
    comment_data.close()

def white_list():


def edit_bulk_comments(username):
    comments = get_comments(username)
    length = len(comments)
    print(length)
    for data in comments:
        print(data['id'])
        export_comment(data)

edit_bulk_comments("ypmihc400")