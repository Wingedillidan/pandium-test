from hubspot3.contacts import ContactsClient
from hubspot3.engagements import EngagementsClient

import tweepy
import os
import json

TWITTER_CONSUMER_KEY = os.environ['PIS_TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['PIS_TWITTER_CONSUMER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['PIS_TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_SECRET = os.environ['PIS_TWITTER_ACCESS_SECRET']

HUBSPOT_TOKEN = os.environ['PIS_HUBSPOT_HAPIKEY']

# Twitter Client Setup
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

TwitterClient = tweepy.API(auth)

# HubSpot Client Setup
HubspotContactsClient = ContactsClient(api_key=HUBSPOT_TOKEN)
HubspotEngagementsClient = EngagementsClient(api_key=HUBSPOT_TOKEN)

# Get mentioned tweets
twitter_mentions = TwitterClient.mentions_timeline()

print(twitter_mentions)

# Get hubspot contacts
# hubspot_contacts = HubspotContactsClient.get_all()

for mention in twitter_mentions:
    # hubspot_contact = HubspotContactsClient.get_contact_by_email(mention.user.name)

    # if not hubspot_contact:
    data = [
        {
            "property": "twitterId",
            "value": mention.user.id
        }]

    hubspot_contact = HubspotContactsClient.create_or_update_a_contact(f"{mention.user.name}@nyu.edu",
        data=json.dumps(data)
    )

    print(hubspot_contact)
    # HubspotEngagementsClient.create(data={

    # })

