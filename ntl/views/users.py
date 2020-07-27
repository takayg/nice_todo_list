from flask import request, redirect, url_for, render_template, flash, session
from ntl import app, db
from ntl.models.create import Create
from PIL import Image, ImageDraw, ImageFont
from flask import send_from_directory

import os

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

        image = Image.open('ntl/' + entry.directory)
        draw = ImageDraw.Draw(image)
        for name in sentence_name:
            sentences.append(request.form[name])

        # タイトルのフォント、サイズ
        font = ImageFont.truetype("YuGothL.ttc", size=45)
        image_width, image_height = image.size
        title_width, title_height = draw.textsize("ｘｘｘｘｘｘｘ", font=font)
        # タイトルのx座標
        start_x_point = image_width/2 - title_width/2
        # タイトルの書き込み
        draw.text((start_x_point, title_height*2), title1, fill=(255,0,0), font=font)
        draw.text((start_x_point, title_height*3), title2, fill=(255,0,0), font=font)
        # ボディのフォント、サイズ
        font = ImageFont.truetype("YuGothL.ttc", size=25)
        image_width, image_height = image.size
        body_width, body_height = draw.textsize("ｘｘｘｘｘｘｘｘｘｘｘｘ", font=font)
        # ボディのxy座標
        start_x_point = 30
        start_y_point = title_height * 5
        # ボディの書き込み
        for sentence in sentences:
            draw.text((start_x_point, start_y_point), " " + sentence, fill=(255,0,0), font=font)
            start_y_point += body_height*1.5
        image.save('./ntl/static/images/new_image.png')
        directory = '/static/images/new_image.png'
    
        return render_template('users/download.html', directory=directory)
    return render_template('users/make_image.html', entry=entry)
