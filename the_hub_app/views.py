import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .models import 
from .keys import api_keys
import tweepy

def home(request):
    return render(request, 'pages/home.html')

def login(request):
    return render(request, 'pages/login.html')

def about(request):
    return render(request, 'pages/about.html')



def view_function(request):
    # Replace these values with your API key and secret
    api_key = 'OFYPwKn1Nd3Fli9Ve86h25bhI'
    api_secret = 'siKZ72y6C9r1YcX79RARH3tX9penOMChw9T2lwfivXHzDSWR2P'

    # Authenticate with the Twitter API
    auth = tweepy.AppAuthHandler(api_key, api_secret)
    api = tweepy.API(auth)

    # Retrieve the tweet or timeline
    tweet = api.get_status('TWEET_ID')  # for a single tweet
    timeline = api.user_timeline('USERNAME')  # for a user timeline

    return render(request, 'template.html', {'tweet': tweet, 'timeline': timeline})

def reddit(request):

    url = "http://www.reddit.com/r/random.json"
    headers = {'User-Agent': 'jeff926'}
    response = requests.get(url, headers=headers)
    data = response.json()
    selftext = data["data"]["children"][0]["data"]["selftext"]
    sub = data["data"]["children"][0]["data"]["subreddit"]
    subPrefix = data["data"]["children"][0]["data"]["subreddit_name_prefixed"]

    print(sub, selftext, subPrefix)
    context = {'data': data, 'sub':sub, 'selftext':selftext, 'subPrefix': subPrefix}
    return render(request, 'pages/reddit.html', context,)


def news(request):
    news_api_key = api_keys()
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key['news']}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    print(data)
    context = {'data': data}
    return render(request, 'pages/news.html', context)

def social(request):
    return render(request, 'pages/social.html')

def games(request):
    return render(request, 'pages/games.html')
    
def twitter(request):
    if request.method == 'GET':
        return render(request, 'pages/twitter.html')
    elif request.method == 'POST':
        username = request.POST['username']
        print(username)
        url= f"https://twitter.com/{username}?ref_src=twsrc%5Etfw"
        return render(request, 'pages/twitter.html', {'url': url})

def sports(request):
    url = "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=2b842165635846d78fb9a2a7bfe21b38"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    print(data)
    context = {'data': data}
    return render(request, 'pages/sports.html', context)


def technology(request):
    url = "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=2b842165635846d78fb9a2a7bfe21b38"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    print(data)
    context = {'data': data}
    return render(request, 'pages/technology.html', context)
