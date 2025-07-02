import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()

twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
)


def scrape_user_tweets(username, num_tweets=5, mock: bool = False):
    """
    Scrapes a twitter user's original tweets and returns them as a list of dic.
    Each dic has 3 fields: time_posted (relative to now), text, and url.
    """
    tweet_list = []

    if mock:
        MOCK_TWEETS = "https://gist.githubusercontent.com/emarco177/9d4fdd52dc432c72937c6e383dd1c7cc/raw/1675c4b1595ec0ddd8208544a4f915769465ed6a/eden-marco-tweets.json"
        tweets = requests.get(MOCK_TWEETS, timeout=5).json()
        print(tweets)

    else:
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_users_tweets(
            id=user_id, max_results=num_tweets, exclude=["retweets, replies"]
        )

    for tweet in tweets:
        tweet_dict = {
            "text": tweet.get("text", ""),
            "url": f"https://twitter.com/{username}/status/{tweet.get('id', '')}",
        }
        tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":

    tweets = scrape_user_tweets(username="afarghaly10", mock=True)
    print(tweets)
