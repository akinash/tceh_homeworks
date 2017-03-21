# -*- coding: utf-8 -*-

from wtforms_alchemy import ModelForm

from models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
