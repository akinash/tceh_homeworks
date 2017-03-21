# -*- coding: utf-8 -*-

from datetime import date

from app import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(140), nullable=False)
    comment = db.Column(db.String(3000), nullable=False)
    datetime = db.Column(db.Date, default=date.today)
