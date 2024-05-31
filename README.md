# allianz

Given the name of a subfeddit, the fastapi application returns a list of the most recent comments along with their unique identifiers, text, polarity score, and classification (positive, negative or neutral).
For sentiment analysis Textblob has been used from textblob library 
The API also allows for optional filtering by a specific time range and sorting the results by the comments' polarity score.

## To execute:
```
docker compose up --build
```
## Results
API: 
```
curl -X 'GET' \
  'http://localhost:8085/comment?subfeddit_id=2&skip=0&limit=25&sort_polarity=false&start_time=1767451&end_time=1767451' \
  -H 'accept: application/json'
```
### Sentiment Analysis Reddit BASE API 
![alt text](https://github.com/ParasHarnagle/allianz/blob/main/resources/1.png)
![alt text](https://github.com/ParasHarnagle/allianz/blob/main/resources/2.png)

### Result with sorted flag
![alt text](https://github.com/ParasHarnagle/allianz/blob/main/resources/3.png)
