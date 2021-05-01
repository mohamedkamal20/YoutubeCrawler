from Crawler import db


class Channel(db.Model):

    id = db.Column(
        db.String(100),
        primary_key=True
    )
    name = db.Column(
        db.String(255),
        nullable=False
    )


class Playlist(db.Model):

    id = db.Column(
        db.String(100),
        primary_key=True
    )
    name = db.Column(
        db.String(255),
        nullable=False
    )
    channel_id = db.Column(
        db.String(100),
        nullable=True
    )


class Video(db.Model):

    id = db.Column(
        db.String(100),
        primary_key=True,
    )
    playlist_id = db.Column(
        db.String(100),
        nullable=False
    )
    url = db.Column(
        db.String(255),
        nullable=False
    )
    title = db.Column(
        db.String(255),
        nullable=False
    )
    duration = db.Column(
        db.String(10),
        nullable=False
    )
    views = db.Column(
        db.Integer,
        nullable=False
    )
    thumbnail_url = db.Column(
        db.String(255),
        nullable=False
    )
    original_url = db.Column(
        db.String(255),
        nullable=False
    )