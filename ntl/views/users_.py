from flask import request, redirect, url_for, render_template, flash, session
from ntl import app, db
from ntl.models.create import Create
from PIL import Image, ImageDraw, ImageFont
from flask import send_from_directory
@app.route('/')
def show_index():
    entries = Create.query.order_by(Create.id.desc()).all()
    return render_template('users/index.html', entries=entries)

@app.route('/make/<int:id>', methods=['GET', 'POST'])
def make_image(id):
    entry = Create.query.get(id)
    if request.method == 'POST':
        title1 = request.form['title1']
        title2 = request.form['title2']
        sentence_name = ['sentence' + str(x) for x in range(1, 11)]
        sentences = []
        for name in sentence_name:
            sentences.append(request.form[name])
        return render_template('users/download.html', title1=title1, title2=title2, sentences=sentences)
    return render_template('users/make_image.html', entry=entry)
