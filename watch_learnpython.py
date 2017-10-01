import time
import sys
import os
import webbrowser
from praw import Reddit


reddit = Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent='desktop:None:v0.0 (by /u/A3gis)'
)

seen_submissions = set()
while True:
    for submission in reddit.subreddit('learnpython').new(limit=5):
        if submission.num_comments == 0 and submission.url not in seen_submissions:
            seen_submissions.add(submission.url)
            webbrowser.open_new_tab(submission.url)
    
    time.sleep(60)
