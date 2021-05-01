from flask import jsonify, request

from Crawler import app
from Crawler.youtube_api import get_playlist_videos, get_channel_videos


@app.route('/api/crawl_playlist', methods=['POST'], strict_slashes=False)
def get_playlist_details():
    try:
        playlist_id = str(request.args.get('playlist_url').split('list=')[1])
        download_videos = bool(request.args.get('download'))
    except IndexError:
        return "Please enter a valid playlist URL", 500
    videos_details = get_playlist_videos(playlist_id, download=download_videos)

    return jsonify({'playlist': videos_details})


@app.route('/api/crawl_channel', methods=['POST'], strict_slashes=False)
def get_channel_details():
    try:
        channel_id = str(request.args.get('channel_url').split('/')[4])
        download_videos = bool(request.args.get('download'))
    except IndexError:
        return "Please enter a valid channel URL", 500
    videos_details = get_channel_videos(channel_id, download_videos)

    return jsonify({'channel': videos_details})


