import requests

response = requests.get('https://api.rss2json.com/v1/api.json?rss_url=https://www.youtube.com/feeds/videos.xml?channel_id=UCEWIYszywEy8TK4xgfrQbPA').json()

index = 0
video = response['items'][index]

while '#shorts' in video['title']:
    index += 1
    video = response['items'][index]

mrv = video['link']
