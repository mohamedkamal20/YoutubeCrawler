import os

import googleapiclient.discovery
import googleapiclient.errors

from Crawler.database import seed_playlist_videos_to_db, seed_channel_details_to_db

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

developer_key = "AIzaSyC1cdcjHN1QNdJo-7I7XTJysBMAtAiqrs0"
api_service_name = "youtube"
api_version = "v3"


def get_playlist_videos(playlist_id, playlist_name="playlist", channel_id=None, download=False):

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)

    playlist_list_api = youtube.playlistItems().list(
        part="contentDetails",
        playlistId="{}".format(playlist_id),
        fields="items/contentDetails(videoId)"
    )
    try:
        playlist_list_response = playlist_list_api.execute()

        videos_id = [video[u'contentDetails'][u'videoId'] for video in playlist_list_response[u'items']]

        videos_details = []

        for video_id in videos_id:
            video_details_api = youtube.videos().list(
                part="id,snippet,contentDetails,statistics",
                id="{}".format(video_id),
                fields="items(id,snippet(title,thumbnails(default,high)),contentDetails(duration),statistics(viewCount))"
            )

            video_details_response = video_details_api.execute()
            videos_details.append(video_details_response)

        seed_playlist_videos_to_db(videos_details, playlist_id, playlist_name, channel_id, download)

        return videos_details
    except:
        return None


def get_channel_videos(channel_id, download=False):

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)

    channel_playlists_api = youtube.playlists().list(
        part="snippet,contentDetails,id",
        channelId="{}".format(channel_id),
        maxResults=5,
        fields="items(id,snippet(title,channelTitle))"
    )
    try:
        channel_playlists_response = channel_playlists_api.execute()
        channel_name = str(channel_playlists_response[u'items'][0][u'snippet']['channelTitle'])

        seed_channel_details_to_db(channel_id, channel_name)

        video_details = []

        for playlist in channel_playlists_response[u'items']:
            playlist_id = playlist[u'id']
            playlist_name = playlist[u'snippet'][u'title']

            playlist_result = get_playlist_videos(playlist_id, playlist_name, channel_id, download)
            video_details.append(playlist_result)

        return video_details
    except:
        return None




