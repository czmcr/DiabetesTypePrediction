import praw
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()

def create_reddit_instance():
    
    reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                         client_secret=os.getenv('CLIENT_SECRET'),
                         user_agent='webScraping')
    return reddit

def fetch_diabetes_posts(reddit, subreddit='all', query='diabetes in adults', limit=1000):
    """Fetch posts related to diabetes from specified subreddit using a search query."""
    posts = []
    for post in reddit.subreddit(subreddit).search(query, limit=limit):
        posts.append([post.title, post.selftext])
    return pd.DataFrame(posts, columns=['title', 'body'])

def save_posts_to_excel(posts_df, file_path='diabetes_posts.xlsx'):
    """Save the fetched posts DataFrame to an Excel file."""
    posts_df.to_excel(file_path, index=False, encoding='utf-8')
    

testing 

# Example usage
# if __name__ == '__main__':
#     reddit = create_reddit_instance()
#     posts_df = fetch_diabetes_posts(reddit)
#     save_posts_to_excel(posts_df)
