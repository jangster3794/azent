"""Data models."""
from . import db
from datetime import datetime

class Universities(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'universities'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    alpha_two_code = db.Column(
        db.String(2),
        index=False,
        nullable=False
    )
    country = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    domain = db.Column(
        db.String,
        index=True,
        unique=True,
        nullable=False
    )
    name = db.Column(
        db.String,
        index=True,
        unique=False,
        nullable=False
    )
    web_page = db.Column(
        db.String,
        index=True,
        unique=True,
        nullable=False
    )
    created_at = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        default=datetime.utcnow()
    )

    def __repr__(self):
        return '<University {}>'.format(self.name)