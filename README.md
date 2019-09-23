# r/AyyMD's lists of approval and unapproval

Got this idea from a Reddit comment on r/AyyMD. Go figure. Very simple Python code, using the PRAW library and some regex fun-ness. Only intended to be built and run once.

The libraries used are [PRAW](https://pypi.org/project/praw/) and [dotenv](https://pypi.org/project/python-dotenv/). The Reddit API details (client ID etc) are stored in a .env file in order to make deployment smoother (and also make sure I don't god damn accidentally upload them to this repo).