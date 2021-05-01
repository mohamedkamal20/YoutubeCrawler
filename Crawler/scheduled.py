from Crawler.database import get_current_channel_id, get_current_playlist_id
from Crawler.youtube_api import get_channel_videos, get_playlist_videos


def scheduled_task():
    channel_id = get_current_channel_id()
    if channel_id is None:
        playlist_id = get_current_playlist_id()
        if playlist_id is not None:
            get_playlist_videos(playlist_id)
    else:
        get_channel_videos(channel_id)
