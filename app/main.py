from fastapi import FastAPI, HTTPException
import logging
import requests
from pydantic import BaseModel
from app.sentiment import sent_analysis
import os
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

FEDDIT_SERVICE_NAME = os.getenv("FEDDIT_SERVICE_NAME", "feddit")
FEDDIT_API_URL = f"http://{FEDDIT_SERVICE_NAME}:8080"
app = FastAPI(
    title="feddit allianz",
    version='1.0',
    description="Sentiment Analysis of feddit"
)

class Comment(BaseModel):
    id: int
    text: str
    polarity_score: float
    classification: str

@app.get("/comment",response_model=list[Comment])
async def sentiment_feddit(subfeddit_id, skip: int=0,limit: int=25,sort_polarity=False):
    """
    Fetch comments for a subfeddit and perform sentiment analysis.

    :param subfeddit_id: The ID of the subfeddit to fetch comments from.
    :param skip: Number of comments to skip.
    :param limit: Maximum number of comments to return.
    :param sort_polarity: Whether to sort comments by polarity score.
    :return: List of comments with sentiment analysis results.
    """
    url = f"{FEDDIT_API_URL}/api/v1/comments/?subfeddit_id={subfeddit_id}&skip={skip}&limit={limit}"
    logging.debug(f"Constructed URL: {url}")
    resp = requests.get(url)
    logging.debug(f"Response status code: {resp.status_code}")
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code,
                            detail="error fetching comments")
    data = resp.json()["comments"]
    logging.debug(f"Response data: {data}")
    comments = []
    for comment in data:
        sentiment = sent_analysis(comment['text'])
        comments.append({
            "id": comment['id'],
            "text": comment['text'],
            "polarity_score": sentiment['polarity_score'],
            "classification": sentiment['classification']
        })

    
    if sort_polarity:
        comments = sorted(comments, key = lambda x:x['polarity_score'])
    return comments[:limit]

