from Crawler import db
from Crawler.models import Playlist, Video, Channel
from Crawler.utilities import save_image, remove_image


def seed_playlist_videos_to_db(videos_details, playlist_id, playlist_name="playlist", channel_id=None):
    existing_playlist = Playlist.query.filter_by(id=playlist_id).first()
    if existing_playlist is None:
        playlist = Playlist(id="{}".format(playlist_id), name=playlist_name, channel_id=channel_id)
        db.session.add(playlist)
    else:
        existing_playlist.name = playlist_name
        existing_playlist.channel_id = channel_id

    db.session.commit()

    for item in videos_details:
        thumbnail_url = str(item['items'][0]['snippet']['thumbnails']['default']['url'])
        original_url = str(item['items'][0]['snippet']['thumbnails']['high']['url'])
        duration = str(item['items'][0]['contentDetails']['duration'])
        views = int(item['items'][0]['statistics']['viewCount'])
        title = str(item['items'][0]['snippet']['title'])
        video_id = str(item['items'][0]['id'])

        existing_video = Video.query.filter_by(id=video_id).first()

        if existing_video is None:
            video = Video(id=video_id,
                          playlist_id="{}".format(playlist_id),
                          title=title,
                          views=views,
                          duration=duration,
                          thumbnail_url="{}".format(save_image(thumbnail_url, False)),
                          original_url="{}".format(save_image(original_url, True)),
                          url="https://www.youtube.com/watch?v={}".format(video_id))

            db.session.add(video)
        else:
            existing_video.playlist_id = str(playlist_id)
            existing_video.title = title
            existing_video.duration = duration
            existing_video.views = views

            remove_image(existing_video.thumbnail_url, False)
            remove_image(existing_video.original_url, True)

            existing_video.thumbnail_url = "{}".format(save_image(thumbnail_url, False))
            existing_video.original_url = "{}".format(save_image(original_url, True))

    db.session.commit()


def seed_channel_details_to_db(channel_id, channel_name):
    existing_channel = Channel.query.filter_by(id=channel_id).first()
    if existing_channel is None:
        channel = Channel(id="{}".format(channel_id), name=channel_name)
        db.session.add(channel)
    else:
        existing_channel.name = channel_name
    db.session.commit()


def get_current_channel_id():
    current_channel = Channel.query.first()
    return current_channel.id if current_channel is not None else None


def get_current_playlist_id():
    current_playlist = Playlist.query.first()
    return current_playlist.id if current_playlist is not None else None




