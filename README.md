# watch-learnpython
Opens the latest questions from /r/learnpython in your browser

## Installation Instructions

1. Clone this repo
2. Install required packages:

```
pip install --user PyQt5
pip install --user praw
```

3. Set environment variables for accessing the Reddit API

```
export REDDIT_CLIENT_ID=get this from https://www.reddit.com/prefs/apps
export REDDIT_CLIENT_SECRET=get this from https://www.reddit.com/prefs/apps
```

(On Windows, use `set` instead of `export`)

4. Run the script

```
python watch_learnpython.py
```
