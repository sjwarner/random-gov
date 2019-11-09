import sys

import requests
from bs4 import BeautifulSoup

import boto3
import json

import tweepy

def resolve_page(base_url):
    resolved_page = requests.get(base_url)
    return resolved_page

def fetch_api_keys():
    secrets = boto3.client('secretsmanager')
    api_keys = json.loads(secrets.get_secret_value(SecretId='RandomGovTwitter')['SecretString'])
    return api_keys

def tweet_url(resolved_page, api_keys):
    auth = tweepy.OAuthHandler(api_keys['RandomGovConsumerKey'], api_keys['RandomGovConsumerSecret'])
    auth.set_access_token(api_keys['RandomGovAccessToken'], api_keys['RandomGovAccessTokenSecret'])
    api = tweepy.API(auth)

    soup = BeautifulSoup(resolved_page.content, "html.parser")
    if soup.title:
        title = soup.title + ' '
    else:
        title = 'Selected page '

    api.update_status(title + resolved_page.url)

def handler(event, handler):
    resolved_page=(resolve_page('https://gov.uk/random'))
    api_keys=fetch_api_keys()
    tweet_url(resolved_page, api_keys)
