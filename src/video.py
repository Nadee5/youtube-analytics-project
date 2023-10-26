import os
import json

from googleapiclient.discovery import build

api_key: str = os.getenv('YOUTUBE_API_KEY')  # YOUTUBE_API_KEY скопирован из гугла и вставлен в переменные окружения

youtube = build('youtube', 'v3', developerKey=api_key)  # создать специальный объект для работы с API


class Video:
    """Класс для ютуб_видео"""

    def __init__(self, video_id):

            self.video_id = video_id
            self.video_info = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',id=video_id).execute()

            try:
                self.title = self.video_info['items'][0]['snippet']['title']
                self.url = 'https://youtu.be/' + self.video_id
                self.view_count = self.video_info['items'][0]['statistics']['viewCount']
                self.like_count = self.video_info['items'][0]['statistics']['likeCount']

            except IndexError:
                self.title = None
                self.url = None
                self.view_count = None
                self.like_count = None


    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):
    
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.playlist_id = 'https://www.youtube.com/playlist?list=' + self.playlist_id

