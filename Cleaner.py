import praw
import requests
import csv
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
# TODO: cron job - automate
# TODO: whitelist by gilded,subreddit,content,score,awards
# TODO: delete submissions

class Cleaner:
    def __init__(self):
        self.reddit = praw.Reddit(client_id=config.get("connection", "client_id"),
                                  client_secret=config.get("connection", "client_secret"),
                                  password=config.get("connection", "password"),
                                  user_agent=config.get("connection", "user_agent"),
                                  username=config.get("connection", "username"))

    @staticmethod
    def get_comments(username):
        link = ("https://api.pushshift.io/reddit/search/comment/?author=" + username)
        r = requests.get(link).json()
        comments = r['data']
        return comments

    def edit_comments(self, link):
        comment = self.reddit.comment(id=link)
        newMessage = "new comment here"
        comment.edit(newMessage)

    def delete_coments(self, link):
        comment = self.reddit.comment(id=link)
        comment.delete()

    @staticmethod
    def export_comment(comment):
        values = [comment['author'], comment['subreddit'], comment['body']]
        comment_data = open('CommentData.csv', 'a')  # open file for writing
        csvwriter = csv.writer(comment_data)
        csvwriter.writerow(values)
        comment_data.close()

    def white_list(self, link):
        # 'created' distinguished, gilded, score subreddit/#subreddit_id gilded #gildings
        comment = self.reddit.comment(id=link)
        subreddit = comment.subreddit
        distinguished = comment.distinguished

        print(comment.distinguished)
        pass

    def edit_bulk_comments(self, username):
        comments = self.get_comments(username)
        list = []
        for data in comments:
            list.append(str(data))
            self.export_comment(data)
        return list


x = Cleaner()

