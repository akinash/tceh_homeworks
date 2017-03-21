# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy


import config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/comment', methods=['POST'])
def comment():
    from models import Comment
    from forms import CommentForm

    form = CommentForm(request.form)

    if form.validate():
        comment = Comment(**form.data)
        db.session.add(comment)
        db.session.commit()
        result = {"status":True, "statusText": "Всё прошло успешно"}
    else:
        flash(str(form.errors))
        result = {"status": False, "errors": form.errors}

    return jsonify(result)


@app.route('/', methods=['GET'])
def index():
    from forms import CommentForm

    form = CommentForm()

    return render_template('index.html', form=form)


if __name__ == '__main__':
    from models import *
    db.create_all()

    app.run()
