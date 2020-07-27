from flask import request, redirect, url_for, render_template, flash, session
from ntl import app, db
from ntl.models.create import Create
from PIL import Image

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('Welcome!')
            return redirect(url_for('creator'))
    return render_template('creators/login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Thank you!')
    return redirect(url_for('show_index'))

@app.route('/creator')
def creator():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('creators/creator.html')

@app.route('/creator/add_image', methods=['POST'])
def add_image():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Create(
        title=request.form['title'],
        name=request.form['name']
    )
    file = Image.open(request.files['file'])
    image_title = request.form['title'] + '.png'
    image_dir = './ntl/static/images/'
    file.save(image_dir + image_title)
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_index'))
    
@app.route('/creator/delete', methods=['GET', 'POST'])
def delete():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        if password != app.config['DELETE_PASSWORD']:
            flash('パスワードが違います')
        else:
            entry = Create.query.get(id)
            db.session.delete(entry)
            db.session.commit()
            flash('削除されました')
    return render_template('creators/delete.html')
    
    