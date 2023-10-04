import json
import os

from googleapiclient.discovery import build

# api_key: str = os.getenv('YOUTUBE_API_KEY') # YOUTUBE_API_KEY скопирован из гугла и вставлен в переменные окружения
#
# youtube = build('youtube', 'v3', developerKey=api_key) # создать специальный объект для работы с API


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YOUTUBE_API_KEY')  # YOUTUBE_API_KEY скопирован из гугла и вставлен в переменные окружения

    youtube = build('youtube', 'v3', developerKey=api_key)  # создать специальный объект для работы с API

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscriber_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel_info, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        """Возвращает приватный инициализированный id канала."""
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        return cls.youtube

    def to_json(self, filename):
        """Сохраняет в файл значения атрибутов экземпляра `Channel`."""
        with open(filename, 'w', encoding='utf-8') as file:
            dict_info = {
                'channel_id': self.__channel_id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subscriber_count': self.subscriber_count,
                'video_count': self.video_count,
                'view_count': self.view_count,
            }
            json.dump(dict_info, file, ensure_ascii=False)




