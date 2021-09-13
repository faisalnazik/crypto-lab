import requests, json
from collections import Counter
from dateutil.parser import parse

""" using github Unauthenticated API, Extracting the last_5_languages of a GitHub User"""
github_user = "faisalnazik"
endpoint = f"https://api.github.com/users/{github_user}/repos"
repos = json.loads(requests.get(endpoint).text)

""" 
The only issue is that the dates in the response are strings:  "created_at": "2013-07-05T02:02:28Z" 
so we’ll need to install one: python -m pip install python-dateutil
"""
dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

last_5_repositories = sorted(repos,
                             key=lambda r: r["pushed_at"],
                             reverse=True)[:5]
last_5_languages = [repo["language"]
                    for repo in last_5_repositories]

print(last_5_languages)

""" Using the Authenticated Twitter APIs """
# python -m pip install twython
# There are quite a few Python Twitter libraries out there, but this is the one that I’ve had the most success working with
# Go to https://developer.twitter.com/. to get credentials

